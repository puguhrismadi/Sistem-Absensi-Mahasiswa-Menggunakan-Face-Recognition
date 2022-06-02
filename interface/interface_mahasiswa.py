#GUI lib
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import fakultas

root = tk.Tk()
root.title("Face Recognition")
root.geometry("360x360")
photo = PhotoImage(file="photos/facial-recognition.png")
root.iconphoto(False, photo)

# Read the Image
image = Image.open("photos/facial-detection.png")
# Reszie the image using resize() method
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.place(x=130,y=40)
# end

# create label Greeting
lbl_Greeting = tk.Label(text="Hi, Welcome to FR System!")
lbl_Greeting.place(x=105,y=180)

# create btn
def inter():
    fakultas.i_fks.fks()

btn_Absensi = tk.Button(text="ABSEN, YUK!", width=25, height=2, command=inter)
btn_Absensi.place(x=80, y=200)

root.mainloop()

