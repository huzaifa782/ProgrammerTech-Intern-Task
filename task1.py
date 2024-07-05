import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x600")

# Create an entry widget to display the input and result
display = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Function to handle button clicks
def on_button_click(char):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + char)

# Function to handle equal button click
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(window, text=button, font=("Arial", 18), command=calculate)
    else:
        btn = tk.Button(window, text=button, font=("Arial", 18), command=lambda b=button: on_button_click(b))
    btn.grid(row=row_val, column=col_val, padx=10, pady=10, ipadx=10, ipady=10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
window.mainloop()

import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x600")

# Create an entry widget to display the input and result
display = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Function to handle button clicks
def on_button_click(char):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + char)

# Function to handle equal button click
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(window, text=button, font=("Arial", 18), command=calculate)
    else:
        btn = tk.Button(window, text=button, font=("Arial", 18), command=lambda b=button: on_button_click(b))
    btn.grid(row=row_val, column=col_val, padx=10, pady=10, ipadx=10, ipady=10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
window.mainloop()
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Create an entry widget to display the input and result
        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button labels
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Create and place buttons
        row_val = 1
        col_val = 0
        for button in buttons:
            if button == '=':
                btn = tk.Button(self.root, text=button, font=("Arial", 18), command=self.calculate)
            else:
                btn = tk.Button(self.root, text=button, font=("Arial", 18), command=lambda b=button: self.on_button_click(b))
            btn.grid(row=row_val, column=col_val, padx=10, pady=10, ipadx=10, ipady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def on_button_click(self, char):
        current_text = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current_text + char)
    
    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

