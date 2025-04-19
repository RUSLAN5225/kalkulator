import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")      #РАЗМЕР
        self.window.resizable(None, None)
        self.window.title("Calculator")      #НАЗВАНИЕ
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = "0"
        self.current_expression = "0"
        self.total_label, self.label = self.create_display_labels()
        self.digits = {7: (1, 1), 8: (1, 2), 9: (1, 3),
                       4: (2, 1), 5: (2, 2), 6: (2, 3),
                       1: (3, 1), 2: (3, 2), 3: (3, 3),
                       0: (4, 2), '.': (4, 1)}
        self.operations = {"/":"\u00F7", "*":"\u00D7", "+":"+", "-":"-"}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.buttons_frame.rowconfigure(0, weight = 1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight = 1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_equals_buttons()

    def run(self):
        self.window.mainloop()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg = "lightgrey")
        frame.pack(expand = True, fill = "both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = "both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame,
                               text=self.total_expression, anchor=tk.E,
                               bg="lightgrey", fg="black",
                               padx=24, font=("Arial", 16))
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame,
                         text=self.current_expression, anchor=tk.E,
                         bg="lightgrey", fg="black",
                         padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text = str(digit), bg = "white", fg = "black", font = ("Arial", 24, "bold"), borderwidth = 0, command = lambda x = digit: self.add_to_expression(x))
            button.grid(row = grid_value[0],column = grid_value[1], sticky = tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="white", fg="black", font=("Arial", 24, "bold"),borderwidth=0, command = lambda x = operator: self.append_operator(x))
            button.grid(row = i, column = 4, sticky = tk.NSEW)
            i+=1

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression =""
        self.update_total_label()
        self.update_label()

    def create_equals_buttons(self):
        button = tk.Button(self.buttons_frame, text="=", bg="white", fg="black", font=("Arial", 24, "bold"),
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()


