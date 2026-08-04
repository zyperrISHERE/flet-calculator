import customtkinter as ctk

# Set up dark/light mode and color theme
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create the modern window
app = ctk.CTk()
app.geometry("400x240")
app.title("Zyperr's Modern Test Window")

def test_action():
    print("CustomTkinter is running perfectly! 🚀")

# CustomTkinter widgets use 'CTk' at the start of their names
button = ctk.CTkButton(app, text="Click My Modern Button", command=test_action)
button.pack(pady=80)

app.mainloop()