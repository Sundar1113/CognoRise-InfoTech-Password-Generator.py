import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Invalid length. Please enter a positive integer.")
            return

        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(tk.END, password)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the password length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

label_length = tk.Label(root, text="Password Length:", font=('Arial', 14))
label_length.pack(pady=10)

entry_length = tk.Entry(root, font=('Arial', 14), bd=5)
entry_length.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", font=('Arial', 14), command=generate_password_button_clicked)
generate_button.pack(pady=20)

entry_password = tk.Entry(root, font=('Arial', 16), bd=10)
entry_password.pack(pady=10)

root.mainloop()
