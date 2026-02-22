# import tkinter as tk

# window = tk.Tk()
# window.title("Hema's Calculator")
# window.geometry("400x400")

# display = tk.Entry(
#     window,
#     font=("Arial", 20),
#     borderwidth=2,
#     relief="solid",
#     justify="right"
# )
# display.pack(fill="x", padx=10, pady=10)

# btn_frame = tk.Frame(window)
# btn_frame.pack()


# def clear():
#     display.delete(0, tk.END)


# def add(value):
#     display.insert(tk.END, value)

# def calculate():
#     try:
#         result = eval(display.get())  # eval calculates string math
#         display.delete(0, tk.END)
#         display.insert(tk.END, result)
#     except:
#         display.delete(0, tk.END)
#         display.insert(tk.END, "Error")


# # First row
# btn7 = tk.Button(btn_frame, text="7", width=5, height=2, font=("Arial", 18), command=lambda: add(7))
# btn7.grid(row=0, column=0, padx=5, pady=5)

# btn8 = tk.Button(btn_frame, text="8", width=5, height=2, font=("Arial", 18), command=lambda: add(8))
# btn8.grid(row=0, column=1, padx=5, pady=5)

# btn9 = tk.Button(btn_frame, text="9", width=5, height=2, font=("Arial", 18), command=lambda: add(9))
# btn9.grid(row=0, column=2, padx=5, pady=5)

# btna = tk.Button(btn_frame, text="+", width=5, height=2, font=("Arial", 18), command=lambda: add("+"))
# btna.grid(row=0, column=3, padx=5, pady=5)

# # Second row
# btn4 = tk.Button(btn_frame, text="4", width=5, height=2, font=("Arial", 18), command=lambda: add(4))
# btn4.grid(row=1, column=0, padx=5, pady=5)

# btn5 = tk.Button(btn_frame, text="5", width=5, height=2, font=("Arial", 18), command=lambda: add(5))
# btn5.grid(row=1, column=1, padx=5, pady=5)

# btn6 = tk.Button(btn_frame, text="6", width=5, height=2, font=("Arial", 18), command=lambda: add(6))
# btn6.grid(row=1, column=2, padx=5, pady=5)

# btns = tk.Button(btn_frame, text="-", width=5, height=2, font=("Arial", 18), command=lambda: add("-"))
# btns.grid(row=1, column=3, padx=5, pady=5)

# # Third row
# btn1 = tk.Button(btn_frame, text="1", width=5, height=2, font=("Arial", 18), command=lambda: add(1))
# btn1.grid(row=2, column=0, padx=5, pady=5)

# btn2 = tk.Button(btn_frame, text="2", width=5, height=2, font=("Arial", 18), command=lambda: add(2))
# btn2.grid(row=2, column=1, padx=5, pady=5)

# btn3 = tk.Button(btn_frame, text="3", width=5, height=2, font=("Arial", 18), command=lambda: add(3))
# btn3.grid(row=2, column=2, padx=5, pady=5)

# btnm = tk.Button(btn_frame, text="*", width=5, height=2, font=("Arial", 18), command=lambda: add("*"))
# btnm.grid(row=2, column=3, padx=5, pady=5)

# # Fourth row
# btn0 = tk.Button(btn_frame, text="0", width=5, height=2, font=("Arial", 18), command=lambda: add(0))
# btn0.grid(row=3, column=0, padx=5, pady=5)

# btne = tk.Button(btn_frame, text="=", width=5, height=2, font=("Arial", 18), command=calculate)
# btne.grid(row=3, column=1, padx=5, pady=5)

# btnc = tk.Button(btn_frame, text="C", width=5, height=2, font=("Arial", 18), command=clear )
# btnc.grid(row=3, column=2, padx=5, pady=5)

# btnd = tk.Button(btn_frame, text="/", width=5, height=2, font=("Arial", 18), command=lambda: add("/"))
# btnd.grid(row=3, column=3, padx=5, pady=5)

# window.mainloop()

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