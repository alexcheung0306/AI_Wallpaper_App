from tkinter import *

root = Tk()  # create a root widget
root.title("Tk Example") #set the title for the example

root.configure(background="skyblue") #set the background to yellow

#set maximum and minimum size for the window
root.minsize(1000, 800)  # width, height
root.maxsize(1200, 1000)

# set the starting size of the window as well as where it will first appear on the screen 
# by specifying the width, height, x, and y coordinates. 
# If the x and y coordinates aren't set, then the window will show up in the top-left corner, (0,0), of the screen.
root.geometry("1000x800+1000+100")  # width x height + x + y


root.mainloop()