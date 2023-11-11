import tkinter as tk

calculation = " "

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def percent():
    global calculation
    result=eval(calculation) / 100
    calculation = str(result)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
   


root = tk.Tk()
root.geometry("300x275")
root.configure(bg="#17161b")

text_result = tk.Text(root, height=2, width=16, font=("Lora", 24))
text_result.grid(columnspan=5)
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_plus.grid(row=2, column=4)
btn_min = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_min.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_div.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_close.grid(row=5, column=3)
btn_mod = tk.Button(root, text="%", command= percent, width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_mod.grid(row=6, column=2)
btn_dot = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_dot.grid(row=6, column=3)
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Lora", 14), fg = "#fff", bg = "#2a2d36")
btn_clear.grid(row=6, column=1)
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Lora", 14), fg = "#fff", bg = "#3697f5")
btn_equal.grid(row=6, column=4)

root.mainloop()