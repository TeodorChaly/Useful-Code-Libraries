import tkinter as tk
from time import strftime, gmtime

class TimerApp:
    def __init__(self, root):
        self.root = root
        root.title("Timer")

        self.time_label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Начать", command=self.start_timer)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="Пауза", command=self.pause_timer)
        self.pause_button.pack()

        self.running = False
        self.elapsed_time = 0

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def pause_timer(self):
        self.running = False

    def update_timer(self):
        if self.running:
            self.elapsed_time += 1
            time_string = strftime('%H:%M:%S', gmtime(self.elapsed_time))
            self.time_label.config(text=time_string)
            self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
