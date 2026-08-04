"""GUI component"""

from tkinter import *

root = Tk()
root.title("testing")
root.geometry("500x450")
root.resizable(False, False)

# Image initialization using variable 'character_img'
try:
    character_img = PhotoImage(file="characterv2.png")
except Exception:
    character_img = None


# =========================================================================================#
# How I Learnt:
""" """


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
        command=lambda: show_dialogue_screen(game_screen, "Option 1"),
    )
    opt1.grid(row=0, column=0, padx=5, sticky="nsew")

    opt2 = Button(
        cards_frame,
        text="Option 2",
        bg="#f0f0f0",
        font=("Arial", 12, "bold"),
        bd=2,
        relief="groove",
        command=lambda: show_dialogue_screen(game_screen, "Option 2"),
    )
    opt2.grid(row=0, column=1, padx=5, sticky="nsew")

    opt3 = Button(
        cards_frame,
        text="Option 3",
        bg="#f0f0f0",
        font=("Arial", 12, "bold"),
        bd=2,
        relief="groove",
        command=lambda: show_dialogue_screen(game_screen, "Option 3"),
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
        command=lambda: show_dialogue_screen(game_screen, "Scavenge"),
    )
    scavenge_btn.pack(side=LEFT)

    rest_btn = Button(
        Alt_button,
        text="Rest",
        bg="#e0e0e0",
        font=("Arial", 10, "bold"),
        padx=10,
        command=lambda: show_dialogue_screen(game_screen, "Rest"),
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
# 3 Option Dialogue


def show_dialogue_screen(previous_screen, choice_text):
    previous_screen.pack_forget()

    dialouge_frame = Frame(root, bg="#ffffff")
    dialouge_frame.pack(fill=BOTH, expand=True)

    # Character/Background visuals frame
    scene_frame = Frame(dialouge_frame, bg="#f9f9f9")
    scene_frame.pack(fill=BOTH, expand=True)

    if character_img:
        character_label = Label(scene_frame, image=character_img, bg="#f9f9f9")
    else:
        character_label = Label(
            scene_frame,
            text="[ Character / Scene Image ]",
            font=("Arial", 14, "bold"),
            bg="#f9f9f9",
            fg="#777777",
        )
    character_label.pack(expand=True)

    # Dialogue box container at bottom (height=140)
    dialouge_box = Frame(
        dialouge_frame, bg="#333333", height=140, padx=10, pady=10
    )
    dialouge_box.pack_propagate(False)
    dialouge_box.pack(fill=X, side=BOTTOM)

    # Inner speech bubble frame
    bubble = Frame(dialouge_box, bg="#ffffff", bd=2, relief="solid")
    bubble.pack(fill=BOTH, expand=True)

    # Continue Button packed FIRST at BOTTOM-RIGHT so it is guaranteed to show
    continue_btn = Button(
        bubble,
        text="Continue >",
        bg="black",
        fg="white",
        font=("Arial", 9, "bold"),
        command=lambda: animation_loading(dialouge_frame),
    )
    continue_btn.pack(side=BOTTOM, anchor=SE, padx=8, pady=5)

    # Dialogue Text packed SECOND to fill remaining upper space in bubble
    text_label = Label(
        bubble,
        text=f'You chose "{choice_text}".\nA strange presence approaches you...',
        bg="#ffffff",
        fg="#000000",
        font=("Arial", 10),
        wraplength=420,
        justify=LEFT,
    )
    text_label.pack(side=TOP, anchor=NW, padx=10, pady=5, fill=BOTH, expand=True)


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
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()