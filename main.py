from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

window = Tk()
window.title("Password generator")
window.geometry("500x500+500+150")
image = PhotoImage(file="icon-password.png")
window.iconphoto(False, image)
window.config(bg="#cccccc")


def copy():
    # Clear to clipboard
    window.clipboard_clear()

    # Copy to clipboard
    window.clipboard_append(password_entry.get())


def returned_password():

    try:
        # Clear entry box
        password_entry.delete(0, END)

        # Get password length
        password_length = int(entry.get())

        password = ""

        # Loop throught password length
        for x in range(password_length):
            password += chr(randint(33, 126))

        # Output password to the screen
        password_entry.insert(0, password)

    except ValueError:

        messagebox.showerror("Error", "I'm sorry but something went wrong")


# Label Frame
label = LabelFrame(window, text="How Many Characters?", font=("Calibri", 13))
label.pack(pady=20)

# Create entry box to designate number of character
entry = ttk.Entry(label, font=("Calibri", 20), width=25)
entry.pack()

# Create entry box for returned password
password_entry = Entry(
    window,
    text="",
    font=("Calibri", 14),
    width=35,
    bd=0,
)
password_entry.pack()

# Create a frame
frame = ttk.Frame(window)
frame.pack(pady=20)

# Create Buttons
get_password = ttk.Button(
    frame,
    text="Generate Strong Password",
    command=returned_password,
)
get_password.grid(row=0, column=0)

copy_password = ttk.Button(frame, text="Copy", command=copy)
copy_password.grid(row=0, column=1)

mainloop()
