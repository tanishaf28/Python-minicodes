"""Simple Calculator GUI using Tkinter."""

import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.expression = ""

        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(
            root,
            textvariable=self.display_var,
            justify="right",
            font=("Segoe UI", 18),
            bd=8,
            relief=tk.GROOVE,
            state="readonly",
            readonlybackground="white",
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Button layout
        # Using × and ÷ labels for UI, mapped to * and / internally.
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for text, row, col in buttons:
            tk.Button(
                root,
                text=text,
                width=5,
                height=2,
                font=("Segoe UI", 14),
                command=lambda t=text: self.on_button_click(t),
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(1, 5):
            root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
            self.display_var.set("0")
            return

        if value == "=":
            self.calculate_result()
            return

        mapped = {"×": "*", "÷": "/"}.get(value, value)
        self.expression += mapped
        self.display_var.set(self.expression)

    def calculate_result(self):
        try:
            result = eval(self.expression, {"__builtins__": {}}, {})
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_var.set("Error")


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
