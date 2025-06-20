import tkinter as tk
from tkinter import TclError, ttk
import pyqrcode
from pyqrcode import QRCode
from PIL import Image, ImageTk
import re


def generateQRCode(str):
    if re.match(r'(?:http[s]?:\/\/.)?(?:www\.)?[-a-zA-Z0-9@%._\+~#=]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&\/\/=]*)', str):
        url = pyqrcode.QRCode(str)
        url.png("./img/qrcode.png", scale=8)
        return True
    else:
        print("Incorrect hyperlink")
        return False

def update_qr_image(img):
    try:
        image = Image.open("./img/qrcode.png")
        photo = ImageTk.PhotoImage(image)
        img.config(image=photo)
        img.image = photo
    except FileNotFoundError:
        print("QR Code is not found")

def configure_columns(root):
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

def configure_rows(root):
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

def main_window():
    root = tk.Tk()
    root.title("QR Code Generator - Henry Dampier")
    root.geometry("500x500")
    root.resizable(False, False)
    # Get rid of the minimise/maximise button only on windows
    try:
        root.attributes('-toolwindow', True)
    except TclError:
        print('Removing the minimise and maximise button is only supported on windows')
    root.attributes('-topmost', 1)

    configure_columns(root)
    configure_rows(root)
    title = ttk.Label(root, text="QR Code Generator", font=("Helvetica", 24))
    title.grid(row=0, column=1, sticky=tk.N, pady=10)
    qr = ttk.Label(root, text="QRCode will appear here")
    qr.grid(row=2, column=1, sticky=tk.S)

    link = tk.StringVar()
    website_link = ttk.Entry(root, text="Website Link", font=("Helvetica", 16), textvariable=link)
    website_link.grid(row=1, column=1)
    website_link.focus()
    def on_link_change(*args):
        if generateQRCode(link.get()):
            update_qr_image(qr)
    link.trace_add(
        "write",
        on_link_change
    )


    root.mainloop()
if __name__ == "__main__":
    main_window()