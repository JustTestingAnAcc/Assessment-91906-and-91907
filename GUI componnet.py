'''GUI component'''

from tkinter import *

root = Tk()
root.title("testing")
root.geometry("500x450")
root.resizable(False, False)


def start_game():
    menu_frame.pack_forget()
    button.place_forget() 

    game_frame = Frame(root, )
    game_frame.pack(fill=BOTH, expland=True)

    game_label = Label(
        game_frame, text="GAMING", fg="yellow", bg="#0B7480", font=("Arial", 28, "bold")
    )
    game_label.pack(expand=True)

#----STARTER SCREEN----#
#testing grid

top_frame = Frame(root)
top_frame.pack(fill=X)

bottom_frame = LabelFrame(root, text="Test")
bottom_frame.pack(fill=X, expand=True, padx=10, pady=10)

#Buttons
button = Button(root, text = "Start", bg = "black", fg = "yellow", 
                font = ("Arial", 35, "bold"), command=root.destroy,
                width=10, height=2)
button.pack(pady=10)
button.place(relx = 0.5, rely = 0.5, anchor= CENTER)




root.mainloop()