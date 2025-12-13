import tkinter as tk

# ---------------- FUNCTIONS ----------------
def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(tk.END, result)
    except:
        clear()
        entry.insert(tk.END, "Error")

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Level 5 - GUI Calculator")
root.geometry("320x420")
root.resizable(False, False)

# ---------------- ENTRY ----------------
entry = tk.Entry(
    root,
    font=("Arial", 20),
    borderwidth=5,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# ---------------- BUTTONS ----------------
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for char in row:
        btn = tk.Button(
            row_frame,
            text=char,
            font=("Arial", 16),
            height=2,
            width=5,
            command=lambda c=char: calculate() if c == '=' else press(c)
        )
        btn.pack(side="left", expand=True, fill="both")

# ---------------- CLEAR BUTTON ----------------
clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Arial", 16),
    bg="#ff6666",
    command=clear
)
clear_btn.pack(fill="both", padx=10, pady=10)

# ---------------- MAIN LOOP ----------------
root.mainloop()
