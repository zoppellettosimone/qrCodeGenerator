from tkinter import *
import qrcode
from PIL import Image

def buttonCommand():
    qrGenerator()
    root.destroy()

def qrGenerator():
    #Create qr code
    qr = qrcode.make(URL.get())

    #Name of image
    imgName = "qrcode.png"

    #Save qr code
    qr.save(imgName)
    
    #Open Image
    myImg = Image.open(imgName)
    myImg.show()

#Definition for Tkinter
root = Tk()
root.geometry('380x380')
root.title("QR Code Generator (write by Simone Zoppelletto)")
root.configure(background='#4d0000')

#URL input (YouTube)
label_URL = Label(root, text="Link to transform:", background='#4d0000', foreground="white", padx=10, pady=10).pack()
URL = Entry(root, width = 50)
URL.pack()

#Like Padx, Pady but between Input Label and Button Label
skipLine = Label(root, text="", background='#4d0000', foreground="white").pack()

Button(root, text="Input", command=qrGenerator).pack()

#Footer Credits
footer = Label(root, text="Created by Simone Zoppelletto", background='#4d0000', foreground="white", padx=10, pady=10).pack()

root.mainloop()