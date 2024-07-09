import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError("Password length must be positive.")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Please enter a valid length.\n{ve}")
        return

    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if digits_var.get():
        characters += string.digits
    if punctuation_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Invalid Selection", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly')

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Password Generator", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Define style
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TCheckbutton", font=("Helvetica", 12))

# Create and place the widgets
length_label = ttk.Label(root, text="Enter the desired password length:")
length_label.pack(pady=10)

length_var = tk.StringVar()
length_entry = ttk.Entry(root, textvariable=length_var)
length_entry.pack(pady=5)

letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
punctuation_var = tk.BooleanVar(value=True)

letters_check = ttk.Checkbutton(root, text="Include Letters", variable=letters_var)
letters_check.pack(pady=5)

digits_check = ttk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(pady=5)

punctuation_check = ttk.Checkbutton(root, text="Include Punctuation", variable=punctuation_var)
punctuation_check.pack(pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = ttk.Entry(root, width=50, state='readonly')
password_entry.pack(pady=5)

copy_button = ttk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack(pady=10)

# Run the main loop
root.mainloop()
