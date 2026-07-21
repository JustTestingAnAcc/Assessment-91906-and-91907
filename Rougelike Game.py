'''Assessment 91906 and 91907'''
'''This assessment uses complex programming techniques to develop a computer program, & using complex processes to develop a digital technologies outcome.
This is a roguelike. Choose your own story game and a turn-based action game, similar to DnD, that's developed in Python, using tkinter.'''

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("testing")

#Window Size
root.geometry("550x550")

#testing grid
top_frame = Frame(root)
top_frame.pack(fill=X)

bottom_frame = LabelFrame(root, text="Test")
bottom_frame.pack(fill=X, expand=True, padx=10, pady=10)

#Buttons
button = Button(root, text="Test", width    =25, command=root.destroy)
button.pack()





root.mainloop()