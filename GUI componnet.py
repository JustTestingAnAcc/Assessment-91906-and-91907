"""GUI component"""

from tkinter import *

root = Tk()
root.title("testing")
root.geometry("500x450")
root.resizable(False, False)


# =========================================================================================#
# ==================Animation Loading==================#
def animation_loading(current_frame):
    current_frame.pack_forget()

    frame_load = Frame(root, bg="#1e1e2e")
    frame_load.pack(fill=BOTH, expand=True)

    load_label = Label(
        frame_load,
        text="Traveling...",
        fg="white",
        bg="#1e1e2e",
        font=("Arial", 16, "bold"),
    )
    load_label.pack(pady=(160, 20))

    # widget box
    progress_bg = Frame(frame_load, bg="#444444", width=300, height=18)
    progress_bg.pack_propagate(False)
    progress_bg.pack()

    # widget filling up
    prog_fill = Frame(progress_bg, bg="#0B7480", width=0, height=18)
    prog_fill.pack(side=LEFT, fill=Y)

    # Animation loading bar
    def updt_prog(width=0):
        if width <= 300:
            prog_fill.config(width=width)
            root.after(15, lambda: updt_prog(width + 6))
        else:
            frame_load.pack_forget()
            load_options_screen()

    updt_prog()


# ==================Animation Loading==================#
# =========================================================================================#
# ==================Start game thing==================#
def load_options_screen():
    game_screen = Frame(root, bg="#ffffff")
    game_screen.pack(fill=BOTH, expand=True)

    title_label = Label(
        game_screen,
        text="Choose where to go?",
        bg="#ffffff",
        font=("Arial", 16, "bold"),
    )
    title_label.pack(pady=10)

    # card Frame
    cards_frame = Frame(game_screen, bg="#ffffff")
    cards_frame.pack(fill=BOTH, expand=True, padx=20, pady=5)
    cards_frame.columnconfigure((0, 1, 2), weight=1, uniform="card")
    cards_frame.rowconfigure(0, weight=1)

    # Options
    opt1 = Button(
        cards_frame,
        text="Option 1",
        bg="#f0f0f0",
        font=("Arial", 12, "bold"),
        bd=2,
        relief="groove",
    )
    opt1.grid(row=0, column=0, padx=5, sticky="nsew")

    opt2 = Button(
        cards_frame,
        text="Option 2",
        bg="#f0f0f0",
        font=("Arial", 12, "bold"),
        bd=2,
        relief="groove",
    )
    opt2.grid(row=0, column=1, padx=5, sticky="nsew")

    opt3 = Button(
        cards_frame,
        text="Option 3",
        bg="#f0f0f0",
        font=("Arial", 12, "bold"),
        bd=2,
        relief="groove",
    )
    opt3.grid(row=0, column=2, padx=5, sticky="nsew")

    # Alternative Options
    Alt_button = Frame(game_screen, bg="#ffffff")
    Alt_button.pack(fill=X, padx=20, pady=15)

    scavenge_btn = Button(
        Alt_button,
        text="Scavenge",
        bg="#e0e0e0",
        font=("Arial", 10, "bold"),
        padx=10,
    )
    scavenge_btn.pack(side=LEFT)

    rest_btn = Button(
        Alt_button,
        text="Rest",
        bg="#e0e0e0",
        font=("Arial", 10, "bold"),
        padx=10,
    )
    rest_btn.pack(side=RIGHT)


def start_game():
    top_frame.pack_forget()
    bottom_frame.pack_forget()
    button.place_forget()

    # #Game frame Display
    game_frame = Frame(root, bg="#0B7480")
    game_frame.pack(fill=BOTH, expand=True)

    game_label = Label(
        game_frame,
        text="GAMING",
        fg="yellow",
        bg="#0B7480",
        font=("Arial", 28, "bold"),
    )
    game_label.pack(expand=True)

    # Action bar to trigger loading animation
    action_bar = Frame(game_frame, bg="#333333", pady=10)
    action_bar.pack(fill=X, side=BOTTOM)

    action_btn = Button(
        action_bar,
        text="Explore World",
        font=("Arial", 11, "bold"),
        command=lambda: animation_loading(game_frame),
    )
    action_btn.pack(pady=5)


# ==================Start game thing==================#
# =========================================================================================#


# ----STARTER SCREEN----#
# testing grid

top_frame = Frame(root)
top_frame.pack(fill=X)

bottom_frame = LabelFrame(root, text="Test")
bottom_frame.pack(fill=X, expand=True, padx=10, pady=10)

# Buttons
button = Button(
    root,
    text="Start",
    bg="black",
    fg="yellow",
    font=("Arial", 35, "bold"),
    command=start_game,
    width=10,
    height=2,
)
# button.pack(pady=10)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()