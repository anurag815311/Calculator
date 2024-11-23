import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            expression = str(result)
            input_var.set(expression)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            input_var.set("")
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Main Application Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#f4f4f4")

expression = ""
input_var = tk.StringVar()

# Display Frame
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.pack(expand=True, fill="both")

# Input Field
input_field = tk.Entry(input_frame, textvar=input_var, font=("Arial", 20), bd=5, relief="ridge", justify="right")
input_field.pack(padx=10, pady=10, fill="both")

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#dcdcdc")
buttons_frame.pack(expand=True, fill="both")

# Buttons Layout
button_texts = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

for row in button_texts:
    button_row = tk.Frame(buttons_frame, bg="#dcdcdc")
    button_row.pack(expand=True, fill="both")
    for text in row:
        button = tk.Button(
            button_row, 
            text=text, 
            font=("Arial", 18), 
            relief="groove", 
            border=0, 
            bg="#f9f9f9", 
            fg="black", 
            padx=20, 
            pady=10
        )
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", click)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 14), bg="#ff4d4d", fg="white", padx=20, pady=5)
exit_button.pack(pady=10)

# Start Application
root.mainloop()
