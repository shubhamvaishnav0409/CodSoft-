

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.equation = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.equation, width=25, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        row_val = 1
        col_val = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, width=5, command=lambda text=button_text: self.click(text))
            button.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        equal_button = tk.Button(master, text='=', width=5, command=self.evaluate)
        equal_button.grid(row=5, column=3, padx=5, pady=5)

    def click(self, text):
        if text == 'C':
            self.equation.set('')
        else:
            self.equation.set(self.equation.get() + text)

    def evaluate(self):
        try:
            result = str(eval(self.equation.get()))
            self.equation.set(result)
        except:
            self.equation.set("Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
