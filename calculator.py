import tkinter as tk

window = tk.Tk()
window.title("Hema's Calculator")
window.geometry("380x500")
window.configure(bg="#1e1e2f")
window.resizable(False, False)

# Display
display = tk.Entry(
    window,
    font=("Arial", 28),
    borderwidth=0,
    relief="flat",
    justify="right",
    bg="#2d2d44",
    fg="white",
    insertbackground="white"
)
display.pack(fill="both", padx=15, pady=20, ipady=20)

btn_frame = tk.Frame(window, bg="#1e1e2f")
btn_frame.pack(expand=True, fill="both")

# Make grid responsive
for i in range(4):
    btn_frame.columnconfigure(i, weight=1)

for i in range(4):
    btn_frame.rowconfigure(i, weight=1)

# Functions
def clear():
    display.delete(0, tk.END)

def add(value):
    display.insert(tk.END, value)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Button style
def create_button(text, row, col, command, bg="#3a3a5a"):
    btn = tk.Button(
        btn_frame,
        text=text,
        font=("Arial", 18),
        bg=bg,
        fg="white",
        bd=0,
        activebackground="#5757a6",
        activeforeground="white",
        command=command
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=8, pady=8)

# Buttons
create_button("7", 0, 0, lambda: add(7))
create_button("8", 0, 1, lambda: add(8))
create_button("9", 0, 2, lambda: add(9))
create_button("+", 0, 3, lambda: add("+"), "#ff9500")

create_button("4", 1, 0, lambda: add(4))
create_button("5", 1, 1, lambda: add(5))
create_button("6", 1, 2, lambda: add(6))
create_button("-", 1, 3, lambda: add("-"), "#ff9500")

create_button("1", 2, 0, lambda: add(1))
create_button("2", 2, 1, lambda: add(2))
create_button("3", 2, 2, lambda: add(3))
create_button("*", 2, 3, lambda: add("*"), "#ff9500")

create_button("0", 3, 0, lambda: add(0))
create_button("=", 3, 1, calculate, "#4CAF50")
create_button("C", 3, 2, clear, "#e63946")
create_button("/", 3, 3, lambda: add("/"), "#ff9500")

window.mainloop()