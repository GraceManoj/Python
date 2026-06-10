from tkinter import*
from PIL import Image, ImageTk

root=Tk()
root.title("image")
root.geometry('400x400')

#use image.open to open and identify the given image file.
upload=Image.open("Beautiful-Flowers.jpg")

#convert this iage into tkinter compatible image
image=ImageTk.Photoimage(upload)

#add image to Tkinter label
label=Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label2=Label(root, text="This is how you add image in Tkinter window")
label2.place(x=40, y=360)

root.mainloop()