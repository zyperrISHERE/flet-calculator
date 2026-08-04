import customtkinter as ctk

# --- Styling & Themes ---
ctk.set_appearance_mode("dark")         # Modern dark mode
ctk.set_default_color_theme("blue")     # Base theme accent

# =====================================================================
# 🧠 BACKEND ENGINE (Your Two-Pass Calculation Parser Logic)
# =====================================================================

def clean(user_input):
    user_input = user_input.replace("+", " + ")
    user_input = user_input.replace("-", " - ")
    user_input = user_input.replace("*", " * ")
    user_input = user_input.replace("/", " / ")
    return user_input

def pass1(user_input, new_tokens):
    i = 0
    while i < len(user_input):
        if user_input[i] == "*" or user_input[i] == "/":
            current_op = user_input[i]
            # Safety guards for malformed expressions (e.g., missing numbers)
            if not new_tokens or i + 1 >= len(user_input):
                raise ValueError("Malformed expression")
                
            left_number = float(new_tokens.pop())
            right_number = float(user_input[i+1])
            i = i + 2
            
            if current_op == "*":
                total = left_number * right_number
                new_tokens.append(str(total))
            elif current_op == "/":
                if right_number == 0:
                    raise ZeroDivisionError("Division by Zero")
                total1 = left_number / right_number
                new_tokens.append(str(total1))
        else:
            new_tokens.append(user_input[i]) 
            i = i + 1
    return new_tokens

def pass2(grand_total, new_tokens):
    for i in range(1, len(new_tokens), 2):
        current_op2 = new_tokens[i]
        if i + 1 >= len(new_tokens):
            raise ValueError("Malformed expression")
        current_num = float(new_tokens[i+1])
        
        if current_op2 == "+":
            grand_total = grand_total + current_num
        elif current_op2 == "-":
            grand_total = grand_total - current_num
    return grand_total

# =====================================================================
# 🎨 FRONTEND GUI LAYOUT (CustomTkinter Frame & Windows)
# =====================================================================

class BeautifulCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("Parser Calc")
        self.geometry("360x540")
        self.resizable(False, False)
        self.configure(fg_color="#17171c") # Deep sleek dark background

        self.expression = ""

        # Configure Grid Rows and Columns to scale smoothly
        self.grid_columnconfigure((0, 1, 2, 3), weight=1, pad=8)
        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=1, pad=8)

        # 📺 Display Screen (Read-Only Screen layout)
        self.display = ctk.CTkEntry(
            self, 
            placeholder_text="0", 
            justify="right", 
            font=("Helvetica", 36, "bold"), 
            height=85,
            fg_color="#22222b",
            border_color="#2d2d3a",
            text_color="#ffffff",
            corner_radius=16
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=(25, 15), sticky="nsew")

        # 🔘 Button Configuration Matrix [Text, Row, Col, ColumnSpan]
        button_layouts = [
            ('C', 1, 0, 3),            ('/', 1, 3, 1),
            ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('*', 2, 3, 1),
            ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('-', 3, 3, 1),
            ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('+', 4, 3, 1),
            ('0', 5, 0, 2), ('.', 5, 2, 1), ('=', 5, 3, 1)
        ]

        # Draw buttons dynamically with aesthetic palettes
        for text, row, col, colspan in button_layouts:
            # Determine color palettes based on button function
            if text == 'C':
                bg = "#e53935"
                hover = "#d32f2f"
            elif text == '=':
                bg = "#ff9500" # Premium dynamic orange accent
                hover = "#e08200"
            elif text in ['/', '*', '-', '+']:
                bg = "#2f313d" # Muted layout operators
                hover = "#3e4152"
            else:
                bg = "#24252c" # Soft dark slate for numbers
                hover = "#2f313a"

            btn = ctk.CTkButton(
                self, 
                text=text, 
                font=("Helvetica", 22, "bold"),
                fg_color=bg,
                hover_color=hover,
                text_color="#ffffff",
                height=65,
                corner_radius=16,
                command=lambda t=text: self.on_button_press(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=6, pady=6, sticky="nsew")

    def on_button_press(self, char):
        if char == 'C':
            self.expression = ""
            self.update_screen("0")
        elif char == '=':
            self.run_engine()
        else:
            # Build expression string continuously 
            self.expression += str(char)
            self.update_screen(self.expression)

    def update_screen(self, text):
        self.display.delete(0, ctk.END)
        self.display.insert(0, text)

    def run_engine(self):
        if not self.expression:
            return

        try:
            # 🚀 Fire up your parser backend
            tokens = clean(self.expression).split()
            if not tokens:
                return

            new_tokens = pass1(tokens, [])
            grand_total = float(new_tokens[0])
            final_ans = pass2(grand_total, new_tokens)

            # Clean float layout display (e.g. drop trailing .0 if integer outcome)
            if final_ans.is_integer():
                result_str = str(int(final_ans))
            else:
                result_str = str(round(final_ans, 6))

            self.update_screen(result_str)
            self.expression = result_str # Save answer so user can keep modifying it!

        except ZeroDivisionError:
            self.update_screen("Error: Div by 0")
            self.expression = ""
        except Exception:
            self.update_screen("Syntax Error")
            self.expression = ""

# --- App Entry Point ---
if __name__ == "__main__":
    app = BeautifulCalculator()
    app.mainloop()