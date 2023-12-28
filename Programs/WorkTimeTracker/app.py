import tkinter as tk
from time import strftime, gmtime
from notification import PopupNotification
from tkinter import simpledialog, messagebox
from db_reg_log import register_user, authenticate_user


class TimerApp:
    def __init__(self, root):
        self.root = root
        root.title("Timer")

        self.time_label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="GO", command=self.start_timer)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="PAUSE", command=self.pause_timer)
        self.pause_button.pack()

        self.running = False
        self.elapsed_time = 0
        self.time_last_break = 0
        self.user_authenticated = False
        self.login_or_register()

    def login_or_register(self):
        if not self.user_authenticated:
            action = simpledialog.askstring("Login/Register", "Type 'login' or 'register':")
            email = simpledialog.askstring("Email", "Enter your email:")
            password = simpledialog.askstring("Password", "Enter your password:", show='*')

            if action == 'register':
                # Регистрация пользователя
                register_user(email, password, "Loh", "Odin")  # Здесь должна быть логика для регистрации пользователя
                messagebox.showinfo("Registration", "Registration successful!")
            elif action == 'login':
                # Вход пользователя
                self.user_authenticated = authenticate_user(email,
                                                            password)  # Здесь должна быть логика для входа пользователя
                if self.user_authenticated:
                    messagebox.showinfo("Login", "Login successful!")
                else:
                    messagebox.showerror("Login", "Login failed. Please try again.")
            else:
                messagebox.showerror("Error", "Invalid action. Please type 'login' or 'register'.")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def pause_timer(self):
        self.running = False

    def update_timer(self):
        if self.running:
            TIME_REMAINDER = 10 * 60  # Change time remainder
            self.elapsed_time += 1
            time_string = strftime('%H:%M:%S', gmtime(self.elapsed_time))
            self.time_label.config(text=time_string)

            if self.elapsed_time - self.time_last_break >= TIME_REMAINDER:
                self.show_break_notification()
                self.time_last_break = self.elapsed_time

            self.root.after(1000, self.update_timer)

    def show_break_notification(self):
        PopupNotification(self.root, "It is time for little break!").show()


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
