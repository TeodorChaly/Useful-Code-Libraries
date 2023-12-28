import tkinter as tk
from tkinter import Label, Entry, Button

from Programs.WorkTimeTracker.db_reg_log import register_user, login_user
from Programs.WorkTimeTracker.work_timer import TimerApp


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.create_login_register_form()

    def create_login_register_form(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.first_name_label = Label(self.frame, text="First Name")
        self.first_name_entry = Entry(self.frame)
        self.last_name_label = Label(self.frame, text="Last Name")
        self.last_name_entry = Entry(self.frame)

        self.email_label = Label(self.frame, text="Email")
        self.email_entry = Entry(self.frame)
        self.password_label = Label(self.frame, text="Password")
        self.password_entry = Entry(self.frame, show='*')
        self.submit_button = Button(self.frame, text="Submit", command=self.submit_form)

        self.toggle_button = Button(self.frame, text="Switch to Login", command=self.toggle_form)

        self.is_registration_form = True
        self.update_form_view()

    def toggle_form(self):
        self.is_registration_form = not self.is_registration_form
        self.update_form_view()

    def update_form_view(self):
        for widget in self.frame.winfo_children():
            widget.pack_forget()

        if self.is_registration_form:
            self.first_name_label.pack()
            self.first_name_entry.pack()
            self.last_name_label.pack()
            self.last_name_entry.pack()
            self.email_label.pack()
            self.email_entry.pack()
            self.password_label.pack()
            self.password_entry.pack()
            self.submit_button.pack()
            self.toggle_button.config(text="Switch to Login")
        else:
            self.email_label.pack()
            self.email_entry.pack()
            self.password_label.pack()
            self.password_entry.pack()
            self.submit_button.pack()
            self.toggle_button.config(text="Switch to Register")

        self.toggle_button.pack()

    def submit_form(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if self.is_registration_form:
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            if register_user(email, first_name, last_name, password):
                print("Registering:", first_name, last_name, email, password)
                self.root.destroy()
                app_root = tk.Tk()
                TimerApp(app_root)
        else:
            if login_user(email, password):
                print("Logging in:", email, password)
                self.root.destroy()
                app_root = tk.Tk()
                TimerApp(app_root)
            else:
                print("Wrong email or password")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
