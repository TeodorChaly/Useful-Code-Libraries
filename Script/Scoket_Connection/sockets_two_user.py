import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 57555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []


def message_handler(text):
    text_str = str(text)
    back_text = str(text).replace("%-=-%", ':').encode('utf-8')
    if text_str.count("%-=-%") > 0:
        user = text_str.split('%-=-%')[0]
        message = text_str.split('%-=-%')[1]
        message_reader = message.split(" ")
        try:
            for index in range(len(nicknames)):
                if nicknames[index] == message_reader[0]:
                    print(True)
                    return nicknames[index], str(user + "(private): " + message.replace(nicknames[index], "")).encode(
                        'utf-8')
        except:
            return "all", back_text
    return "all", back_text


def broadcast(message1):
    name, message = message_handler(message1)
    print(name, message)
    if name == "all":
        for client in clients:
            client.send(message)
    else:
        for index in range(len(nicknames)):
            if nicknames[index] == name:
                clients[index].send(message)


# Name  -> port
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print('Server started')
receive()
