# Import the following Modules
from tkinter import *
import csv
import os

root = Tk()
path = Entry(root,width=50)
path.pack()
path.insert(0,"Check Path lll")
# No clue
def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()
# Creates following widgets
def create_widgets(self):
    self.hi_there = Button(self)
    self.hi_there["text"] = "Hello World\n(click me)"
    self.hi_there["command"] = self.say_hi
    self.hi_there.pack(side="top")
    self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
    self.quit.pack(side="bottom")
# Delete this
def say_hi(self):
    print("hi there, everyone!")
# This function checks if your csv file exists 
def check_path_csv():
    # If input is ...
    try:
        trying = open(path.get())
        print("file exists")
    except IOError:
        print("path not accessible")
        
#    if (path.get() == 'lol'):
#        print("lol")
#    # If input isnt...
#    else:
#        print("WTF")

# Start Class Application

Path_button = Button(root, text="Check CSV:", command=check_path_csv)
Path_button.pack()
#Path.pack(side="top",archor="nw")

#T = Text(root,height=1, width=30)
#T.pack(side="top", anchor="nw")
#T.insert(END,"Path:")
#label = Label(root, text="Enter name")

text_widget = Text(root, height=5, width=40,)
 
# Create a scrollbar
scroll_bar = Scrollbar(root)
 
# Pack the scroll bar
# Place it to the right side, using tk.RIGHT
scroll_bar.pack(side="right")
 
# Pack it into our tkinter application
# Place the text widget to the left side
text_widget.pack(side="left")
 
long_text = """This is a multiline string.
We can write this in multiple lines too!
Hello from AskPython. This is the third line.
This is the fourth line. Although the length of the text is longer than
the width, we can use tkinter's scrollbar to solve this problem!
"""

# Insert text into the text widget
text_widget.insert(END, long_text)
root.iconbitmap(r"../CSV_Lens/lens.ico")
# Settings
# Title shown in the window
root.title("CSV Lens")
# Minimum Size of the window
root.minsize(400,400)
# Startup Size of the window
root.geometry("500x500")
# Icon in the window
#os.chdir("/CSV_Lens/code")
#os.getcwd()
#root.iconbitmap('/Lens.ico')
root.configure(background = "#d9d9d9")


#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='/CSV_Lens/Ico/Lens.ico')
# Background color

root.mainloop()