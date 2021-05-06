# Import the following Modules
from tkinter import *
from tkinter import messagebox
import csv
import os

# Variables
Path_right_button_color ="#659658"
Path_right_button_color_clicked = "#006400"

Path_wrong_path_button_color = "#ae0000"
Path_wrong_path_button_color_clicked = "#8B0000"

Path_wrong_file_button_color = "#ae0000"
Path_wrong_file_button_clicked = "#8B0000"

Path_isnt_csv_message = "File is wrong\nTry a file like\n.csv"
Path_is_wrong_message = "Path is wrong\nTry format like\n"+ "F:/User/Code/test.csv"


root = Tk()
path = Entry(root,width=50)
path.pack(side="left",anchor="nw")


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

# This function checks if your path to csv is valid
def check_path_csv():
    # First check if path is valid
    try:
        trying = open(path.get())
        # Change type from Entry to string (to work with endswith)
        path_type = str(path.get())
        # Second check if file ends with csv
        if path_type.endswith('.csv'):
                Path_button.configure(background = Path_right_button_color, activebackground = Path_right_button_color_clicked)
        # If file isnt csv
        else:
                # change color to red
                Path_button.configure(background = Path_wrong_file_button_color, activebackground = Path_wrong_file_button_clicked)
                # Show message wrong filetype
                messagebox.showinfo(title="ERROR",message=Path_isnt_csv_message)
    # If path doesnt work
    except IOError:
        Path_button.configure(background = Path_wrong_button_color, activebackground = Path_wrong_button_color_clicked)
        messagebox.showinfo(title="ERROR",message=Path_is_wrong_message)
    


        
#    if (path.get() == 'lol'):
#        print("lol")
#    # If input isnt...
#    else:
#        print("WTF")

# Start Class Application




Path_button = Button(root, text="Check CSV:", command=check_path_csv,height=1)
Path_button.pack(side="left",anchor="nw")
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