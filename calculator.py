import tkinter as tk


class CuteCalculator:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Cute Calculator")
        self.root.geometry("340x500")
        self.root.configure(bg="#ffe6f2")
        self.root.resizable(False, False)

        self.expression = ""

        self.display_var = tk.StringVar(value="0")

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Comic Sans MS", 28, "bold"),
            bd=0,
            relief="flat",
            justify="right",
            bg="#fff8fc",
            fg="#6b3f5b",
            insertbackground="#6b3f5b",
        )
        display.pack(fill="x", padx=18, pady=(24, 14), ipady=16)

        button_frame = tk.Frame(root, bg="#ffe6f2")
        button_frame.pack(expand=True, fill="both", padx=14, pady=(4, 16))

        rows = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "("],
        ]

        # Add closing bracket as a cute floating button near bottom right.
        close_btn = tk.Button(
            root,
            text=")",
            font=("Comic Sans MS", 16, "bold"),
            bg="#d6f5ff",
            fg="#4a6470",
            bd=0,
            activebackground="#b8ebff",
            activeforeground="#4a6470",
            command=lambda: self.on_click(")"),
        )
        close_btn.place(x=280, y=450, width=40, height=34)

        for r in range(5):
            button_frame.grid_rowconfigure(r, weight=1)
            for c in range(4):
                button_frame.grid_columnconfigure(c, weight=1)
                label = rows[r][c]
                btn = tk.Button(
                    button_frame,
                    text=label,
                    font=("Comic Sans MS", 18, "bold"),
                    bd=0,
                    relief="flat",
                    command=lambda x=label: self.on_click(x),
                )

                if label in {"/", "*", "-", "+", "=", "%"}:
                    btn.configure(bg="#ffd6eb", fg="#7f3b65", activebackground="#ffc2e1")
                elif label in {"C", "⌫"}:
                    btn.configure(bg="#fff0b3", fg="#7f6200", activebackground="#ffe98a")
                else:
                    btn.configure(bg="#d6f5ff", fg="#34505b", activebackground="#b8ebff")

                btn.grid(row=r, column=c, sticky="nsew", padx=6, pady=6, ipady=8)

    def on_click(self, char: str) -> None:
        if char == "C":
            self.expression = ""
            self.display_var.set("0")
        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif char == "=":
            self.calculate()
        else:
            self.expression += char
            self.display_var.set(self.expression)

    def calculate(self) -> None:
        if not self.expression:
            return

        try:
            allowed = set("0123456789+-*/%.() ")
            if any(ch not in allowed for ch in self.expression):
                raise ValueError("Invalid characters")

            result = eval(self.expression, {"__builtins__": {}}, {})
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_var.set("Oops! Try again 💖")


if __name__ == "__main__":
    root = tk.Tk()
    CuteCalculator(root)
    root.mainloop()
