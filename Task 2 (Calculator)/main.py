import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 16), bd=10, relief='ridge', justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

      
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in self.buttons:
            tk.Button(root, text=button, width=5, height=2, font=('Arial', 16), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == '=':
            try: 
                result = str(eval(current_text))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            new_text = current_text + button_text
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
