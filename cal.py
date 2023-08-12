import tkinter as tk

def add():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 + num2)

def subtract():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 - num2)

def multiply():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 * num2)

def divide():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 == 0:
        result.set("Cannot divide by zero")
    else:
        result.set(num1 / num2)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry fields
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

entry_num1.grid(row=0, column=0)
entry_num2.grid(row=0, column=2)

# Buttons
button_add = tk.Button(root, text="Add", command=add)
button_subtract = tk.Button(root, text="Subtract", command=subtract)
button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_divide = tk.Button(root, text="Divide", command=divide)

button_add.grid(row=1, column=0)
button_subtract.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

# Result label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=2, column=0, columnspan=4)

# Start the GUI event loop
root.mainloop()
