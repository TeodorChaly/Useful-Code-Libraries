import tkinter as tk
from tkinter import ttk
import pyperclip
from Super_Dynamic_Cipher import Ciphar
from Super_Dynamic_Decipher import Decipher

# Function to handle the "Copy" button click event
def copy_result():
    result = result_text.get("1.0", "end-1c")  # Get the result from the text box
    if result:
        pyperclip.copy(result)

# Function to handle the program selection
def program_selected(*args):
    input_entry.delete(0, "end")  # Clear the input field
    selected_program = program_var.get()

    if selected_program == "Cipher":
        text_label.config(text="Rules:\n1)Don't use Space\n2)Only English letters")
    else:
        text_label.config(text="Paste an encrypted text\nin the input section!")

# Function to handle the "Process" button click event
def process_input():
    selected_program = program_var.get()
    user_input = input_entry.get()

    if selected_program == "Cipher":
        result = Ciphar(user_input)
    else:
        result = Decipher(user_input)

    result_text.config(state=tk.NORMAL)  # Enable the text field
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)  # Disable the text field
    copy_button.grid(column=0, row=5, padx=10, pady=10)  # Display the "Copy" button below the result

# Create the main window
root = tk.Tk()
root.title("Cipher and Decipher")

# Create a frame for the program selection
program_frame = ttk.Frame(root)
program_frame.grid(column=0, row=0, padx=10, pady=10)

program_var = tk.StringVar()
program_var.set("Cipher")
program_var.trace("w", program_selected)  # Add a trace to clear the input field

cipher_radio = ttk.Radiobutton(program_frame, text="Cipher", variable=program_var, value="Cipher")
decipher_radio = ttk.Radiobutton(program_frame, text="Decipher", variable=program_var, value="Decipher")

cipher_radio.grid(column=0, row=0)
decipher_radio.grid(column=1, row=0)

# Create an entry for user input
input_frame = ttk.Frame(root)
input_frame.grid(column=0, row=1, padx=10, pady=10)

input_label = ttk.Label(input_frame, text="Text:")
input_label.grid(column=0, row=0)

input_entry = ttk.Entry(input_frame, width=40)
input_entry.grid(column=1, row=0)

# Text sections for "Cipher" and "Decipher" modes
text_in_cipher = "Rules:\n1)Don't use Space\n2)Only English letters"
text_in_decipher = "Paste an encrypted text\nin the input section!"

# Create a label to display the text sections
text_label = ttk.Label(root, text=text_in_cipher)
text_label.grid(column=0, row=2, pady=5)

# Create a button to process the input
process_button = ttk.Button(root, text="Process", command=process_input)
process_button.grid(column=0, row=3, pady=10)

# Create a text box for the result (smaller size and non-editable)
result_text = tk.Text(root, width=40, height=5, state=tk.DISABLED)
result_text.grid(column=0, row=4, padx=10, pady=10)

# Create a "Copy" button to copy the result (positioned below the result field)
copy_button = ttk.Button(root, text="Copy Result", command=copy_result)
copy_button.grid(column=0, row=5, padx=10, pady=10)
copy_button.grid_remove()  # Hide the "Copy" button initially

# Start the GUI main loop
root.mainloop()
