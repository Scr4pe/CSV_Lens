# Import the following Modules
from tkinter import *
from tkinter import messagebox
import csv
import os

# Variables
# Variables about the path
Path_right_button_color ="#659658"
Path_right_button_color_clicked = "#006400"
Path_wrong_path_button_color = "#ae0000"
Path_wrong_path_button_color_clicked = "#8B0000"
Path_wrong_file_button_color = "#ae0000"
Path_wrong_file_button_clicked = "#8B0000"
Path_isnt_csv_message = "File is wrong\nTry a file like\nending with .csv"
Path_is_wrong_message = "Path is wrong\nTry format like\n" + "F:/User/Code/test.csv"
skip_button_right_color = "#659658"
skip_button_right_color_clicked = "#006400"
skip_button_wrong_color = "#ae0000"
skip_button_wrong_color_clicked = "#8B0000"
skip_is_string_message = "Input is wrong (string)\nTry input like\nInteger 1 or 2.."
skip_is_unkown_message = "Input is wrong (unkown)\nTry input like\nInteger 1 or 2.."
# No clue
#def __init__(self, master=None):
#    super().__init__(master)
#    self.master = master
#    self.pack()
#    self.create_widgets()
## Creates following widgets
#def create_widgets(self):
#    self.hi_there = Button(self)
#    self.hi_there["text"] = "Hello World\n(click me)"
#    self.hi_there["command"] = self.say_hi
#    self.hi_there.pack(side="top")
#    self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
#    self.quit.pack(side="bottom")
## Delete this
#def say_hi(self):
#    print("hi there, everyone!")

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
        Path_button.configure(background = Path_wrong_path_button_color, activebackground = Path_wrong_path_button_color_clicked)
        messagebox.showinfo(title="ERROR",message=Path_is_wrong_message)

# Ask the user if this is the right start line
def start_lines():
    trying = open(path.get())
    skipping = skip.get()
    # Try value type is integer
    try:
        int(skipping)
        # Change color to green
        skip_button.configure(background = skip_button_right_color, activebackground = skip_button_right_color_clicked)
        # 

        # Open CSV file and ask if this is the first line of data not the header
        csv_file = open(path.get())
        csv_reader = csv.reader(csv_file)
        while (skipping > 0):
            csv_reader = next(csv_reader)
            skipping = skipping - 1
        else:
            # if row in csv_reader:
            messagebox.showinfo(title="Is this data ?",message = csv_reader)    


    # If value type isnt integer or string
    except ValueError:
        # Try value type is string
        try:
            str(skipping)
            # Change color to red
            skip_button.configure(background = skip_button_wrong_color, activebackground = skip_button_wrong_color_clicked)
            # Show message imput is wrong
            messagebox.showinfo(title="ERROR",message=skip_is_string_message)
        # If value isnt string
        except ValueError:
            # Change color of buttom to red
            skip_button.configure(background = skip_button_wrong_color, activebackground = skip_button_wrong_color_clicked)
            # Show message imput is wrong  
            messagebox.showinfo(title="ERROR",message=skip_is_unkown_message)

    # Message the user if this is right
    # Add if statement in the messagebox

# It is the basic informations every Algorithm need from the csv
def Algo_basic():
    # import Path
    print(path_type)
    #




root = Tk()
path = Entry(root,width=30,font="12",borderwidth=2)
path.pack(side="left",anchor="nw")
Path_button = Button(root, text="Check CSV:", command=check_path_csv,height=1,padx=1,pady=1)
Path_button.pack(side="left",anchor="nw")

skip = Entry(root,width=10,font="12",borderwidth=2)
skip.pack(side="left",anchor="nw")
#font="Times 100",height=10,padx=1,pady=1


skip_button = Button(root, text="Skip lines", command=start_lines,height=1,padx=1,pady=1)
skip_button.pack(side="left",anchor="n")

#T = Text(root,height=1, width=30)
#T.pack(side="top", anchor="nw")
#T.insert(END,"Path:")
#label = Label(root, text="Enter name")

#text_widget = Text(root, height=5, width=40,)
 
# Create a scrollbar
#scroll_bar = Scrollbar(root)
 
# Pack the scroll bar
# Place it to the right side, using tk.RIGHT
#scroll_bar.pack(side="right")
 
# Pack it into our tkinter application
# Place the text widget to the left side
#text_widget.pack(side="left")
 
#long_text = """This is a multiline string.
#We can write this in multiple lines too!
#Hello from AskPython. This is the third line.
#This is the fourth line. Although the length of the text is longer than
#the width, we can use tkinter's scrollbar to solve this problem!
#"""

# Insert text into the text widget
#text_widget.insert(END, long_text)
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