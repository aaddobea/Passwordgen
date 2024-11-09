from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import string
import pyperclip

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title('Password Generator')
        self.window.geometry('500x300')
        self.window.config(bg='DeepSkyBlue2')

        # Password options
        self.include_letters = BooleanVar(value=True)
        self.include_numbers = BooleanVar(value=True)
        self.include_symbols = BooleanVar(value=True)

        # Password length
        self.password_length = IntVar(value=12)

        # Component creation
        self.create_widgets()

    def create_widgets(self):
        # Title label
        Label(self.window, text='Password Generator', font=('Helvetica', 20), bg='SlateBlue2', fg='orange red').pack(pady=10)

        # Password display
        self.password_entry = Entry(self.window, font=('sans', 14), bg='white', fg='black', width=35, relief='solid')
        self.password_entry.pack(pady=10)

        # Options frame
        options_frame = Frame(self.window, bg='gray')
        options_frame.pack(pady=5)

        # Character options checkboxes
        Checkbutton(options_frame, text='Include Letters', var=self.include_letters, bg='gray').grid(row=0, column=0, sticky=W)
        Checkbutton(options_frame, text='Include Numbers', var=self.include_numbers, bg='gray').grid(row=0, column=1, sticky=W)
        Checkbutton(options_frame, text='Include Symbols', var=self.include_symbols, bg='gray').grid(row=0, column=2, sticky=W)

        # Password length slider
        Label(self.window, text='Password Length:', bg='gray').pack()
        Scale(self.window, from_=8, to=32, orient=HORIZONTAL, variable=self.password_length).pack()

        # Generate button
        Button(self.window, text="Generate Password", font=('Courrier', 12), bg='white', fg='black', command=self.generate_password).pack(pady=5)

        # Copy to clipboard button
        Button(self.window, text="Copy to Clipboard", font=('Courrier', 10), bg='lightgray', command=self.copy_to_clipboard).pack(pady=5)

    def generate_password(self):
        characters = ""
        if self.include_letters.get():
            characters += string.ascii_letters
        if self.include_numbers.get():
            characters += string.digits
        if self.include_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Selection Error", "Please select at least one character type.")
            return

        password = [choice(characters) for _ in range(self.password_length.get())]
        shuffle(password)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, ''.join(password))

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Copy Error", "No password generated to copy.")

# Run the application
app = App()
app.window.mainloop()
