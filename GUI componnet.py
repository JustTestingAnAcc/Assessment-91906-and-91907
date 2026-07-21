'''GUI component'''

from tkinter import *

root = Tk()
root.title("testing")

#Window Size
root.geometry("500x450")

#testing grid
top_frame = Frame(root)
top_frame.pack(fill=X)

bottom_frame = LabelFrame(root, text="Test")
bottom_frame.pack(fill=X, expand=True, padx=10, pady=10)

#Buttons
button = Button (root, text="Start", width=15, height=4, command=root.destroy, font=("Arial", 25, "bold"))
button.pack(pady=10)
button.place(relx = 0.5, rely = 0.5, anchor= CENTER)



#Prevents user from resizing the Window
root.resizable(False, False)

#Text font


root.mainloop()