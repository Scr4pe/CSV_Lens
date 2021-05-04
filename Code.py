import tkinter as tk
from tkinter import ttk
import csv

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
label = ttk.Label(root, text="Enter name")

text_widget = tk.Text(root, height=5, width=40)
 
# Create a scrollbar
scroll_bar = tk.Scrollbar(root)
 
# Pack the scroll bar
# Place it to the right side, using tk.RIGHT
scroll_bar.pack(side=tk.RIGHT)
 
# Pack it into our tkinter application
# Place the text widget to the left side
text_widget.pack(side=tk.LEFT)
 
long_text = """This is a multiline string.
We can write this in multiple lines too!
Hello from AskPython. This is the third line.
This is the fourth line. Although the length of the text is longer than
the width, we can use tkinter's scrollbar to solve this problem!
"""
 
# Insert text into the text widget
text_widget.insert(tk.END, long_text)

# Settings
# Title shown in the window
root.title("CSV Lens")
# Minimum Size of the window
root.minsize(400,400)
# Startup Size of the window
root.geometry("500x500")
# Icon in the window
root.iconbitmap("Lens.ico")
# Background color
root.configure(background = "#d9d9d9")
#
app = Application(master=root)
app.mainloop()