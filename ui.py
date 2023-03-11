import sys
print(sys.executable)
import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk


root = tk.Tk()  # create a root widget
root.title("Tk Example") #set the title for the example

root.configure(background="skyblue") #set the background to yellow

#set maximum and minimum size for the window
root.minsize(1000, 800)  # width, height
root.maxsize(1200, 1000)

# set the starting size of the window as well as where it will first appear on the screen 
# by specifying the width, height, x, and y coordinates. 
# If the x and y coordinates aren't set, then the window will show up in the top-left corner, (0,0), of the screen.
root.geometry("1000x800+1000+100")  # width x height + x + y


# Create Label in our window
text = tk.Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = tk.Label(root, text="- Maya Angelou")
text2.pack()

# Create a canvas widget
canvas=tk.Canvas(root, width=1000, height=800)
canvas.pack()

# Create an object of tkinter ImageTk
# image = PIL.Image.open("./imgs/bear.jpg")

# img = tk.Label(root, image=img)
# img.pack()

# Add the image in the canvas
# canvas.create_image(900, 700, image=img, anchor="center")

root.mainloop()