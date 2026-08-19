"""GUI component"""

from tkinter import *

root = Tk()
root.title("testing")
root.geometry("500x450")
root.resizable(False, False)

# --- Global Game State ---
current_round = 1
MAX_ROUNDS = 3

# Fixed non-randomized options per round
ROUND_OPTIONS = {
    1: [
        {"text": "(Cave)", "is_combat": True, "event_type": "goblin"},
        {"text": "(Forest)", "is_combat": True, "event_type": "wizard"},
        {"text": "(Plains)", "is_combat": False, "event_type": "sword_rock"},
    ],
    2: [
        {"text": "(Mine)", "is_combat": True, "event_type": "goblin"},
        {"text": "(Lake)", "is_combat": False, "event_type": "sword_rock"},
        {"text": "(Lair)", "is_combat": True, "event_type": "wizard"},
    ],
    3: [
        {"text": "(Ruins)", "is_combat": True, "event_type": "goblin"},
        {"text": "(Temple)", "is_combat": False, "event_type": "sword_rock"},
        {"text": "(Castle)", "is_combat": True, "event_type": "wizard"},
    ],
}

# --- Asset Loading ---
try:
    character_img = PhotoImage(file="character.png")
except Exception:
    character_img = None

try:
    goblin_img = PhotoImage(file="goblinNPC.png")
except Exception:
    goblin_img = None

try:
    wizard_img = PhotoImage(file="wizardDialouge.png")
except Exception:
    wizard_img = None

try:
    sword_rock_img = PhotoImage(file="SwordRock.png")
except Exception:
    sword_rock_img = None


# ==================Animation Loading==================#
def animation_loading(current_frame, next_screen="options"):
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

    progress_bg = Frame(frame_load, bg="#444444", width=300, height=18)
    progress_bg.pack_propagate(False)
    progress_bg.pack()

    prog_fill = Frame(progress_bg, bg="#0B7480", width=0, height=18)
    prog_fill.pack(side=LEFT, fill=Y)

    def updt_prog(width=0):
        if width <= 300:
            prog_fill.config(width=width)
            root.after(15, lambda: updt_prog(width + 6))
        else:
            frame_load.pack_forget()
            if next_screen == "combat_wizard":
                show_combat_screen(enemy_type="wizard")
            elif next_screen == "combat_goblin":
                show_combat_screen(enemy_type="goblin")
            elif next_screen == "victory":
                show_victory_screen()
            else:
                load_options_screen()

    updt_prog()


# ==================Start Game Options (3 FIXED ROUNDS)==================#
def load_options_screen():
    global current_round

    if current_round > MAX_ROUNDS:
        show_victory_screen()
        return

    game_screen = Frame(root, bg="#ffffff")
    game_screen.pack(fill=BOTH, expand=True)

    title_label = Label(
        game_screen,
        text=f"Round {current_round} / {MAX_ROUNDS}: Choose where to go?",
        bg="#ffffff",
        font=("Arial", 14, "bold"),
    )
    title_label.pack(pady=10)

    cards_frame = Frame(game_screen, bg="#ffffff")
    cards_frame.pack(fill=BOTH, expand=True, padx=20, pady=5)
    cards_frame.columnconfigure((0, 1, 2), weight=1, uniform="card")
    cards_frame.rowconfigure(0, weight=1)

    options = ROUND_OPTIONS[current_round]

    for col_index, option in enumerate(options):
        btn_text = f"Option {col_index + 1}\n{option['text']}"

        opt_btn = Button(
            cards_frame,
            text=btn_text,
            bg="#f0f0f0",
            font=("Arial", 10, "bold"),
            bd=2,
            relief="groove",
            command=lambda opt=option, num=col_index + 1: show_dialogue_screen(
                game_screen,
                f"Option {num}",
                is_combat=opt["is_combat"],
                event_type=opt["event_type"],
            ),
        )
        opt_btn.grid(row=0, column=col_index, padx=5, sticky="nsew")

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
    global current_round
    current_round = 1

    top_frame.pack_forget()
    bottom_frame.pack_forget()
    button.place_forget()

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

    action_bar = Frame(game_frame, bg="#333333", pady=10)
    action_bar.pack(fill=X, side=BOTTOM)

    action_btn = Button(
        action_bar,
        text="Explore World",
        font=("Arial", 11, "bold"),
        command=lambda: animation_loading(game_frame),
    )
    action_btn.pack(pady=5)


# ==================Dialogue Screen==================#
def show_dialogue_screen(
    previous_screen, choice_text, is_combat=False, event_type="generic"
):
    previous_screen.pack_forget()

    dialouge_frame = Frame(root, bg="#ffffff")
    dialouge_frame.pack(fill=BOTH, expand=True)

    scene_frame = Frame(dialouge_frame, bg="#f9f9f9")
    scene_frame.pack(fill=BOTH, expand=True)

    if event_type == "sword_rock" and sword_rock_img:
        display_img = sword_rock_img
    elif character_img:
        display_img = character_img
    else:
        display_img = None

    if display_img:
        character_label = Label(scene_frame, image=display_img, bg="#f9f9f9")
    else:
        placeholder_text = (
            "[ MAGIC SWORD IN STONE ]"
            if event_type == "sword_rock"
            else "[ Character / Scene Image ]"
        )
        character_label = Label(
            scene_frame,
            text=placeholder_text,
            font=("Arial", 14, "bold"),
            bg="#f9f9f9",
            fg="#777777",
        )
    character_label.pack(expand=True)

    dialouge_box = Frame(
        dialouge_frame, bg="#333333", height=140, padx=10, pady=10
    )
    dialouge_box.pack_propagate(False)
    dialouge_box.pack(fill=X, side=BOTTOM)

    bubble = Frame(dialouge_box, bg="#ffffff", bd=2, relief="solid")
    bubble.pack(fill=BOTH, expand=True)

    def advance_game():
        global current_round
        if not is_combat:
            current_round += 1

        next_target = (
            f"combat_{event_type}"
            if is_combat
            else ("victory" if current_round > MAX_ROUNDS else "options")
        )
        animation_loading(dialouge_frame, next_screen=next_target)

    continue_btn = Button(
        bubble,
        text="Fight!" if is_combat else "Continue >",
        bg="red" if is_combat else "black",
        fg="white",
        font=("Arial", 9, "bold"),
        command=advance_game,
    )
    continue_btn.pack(side=BOTTOM, anchor=SE, padx=8, pady=5)

    if event_type == "sword_rock":
        msg = "You stumble upon an ancient magical sword deeply embedded in a mysterious rock. It pulses with radiant energy under the sun!"
    elif is_combat:
        enemy_name = "Evil Wizard" if event_type == "wizard" else "Evil Goblin"
        msg = f'You chose "{choice_text}".\nAn {enemy_name} jumps out from the shadows!'
    else:
        msg = f'You chose "{choice_text}".\nA strange presence approaches you...'

    text_label = Label(
        bubble,
        text=msg,
        bg="#ffffff",
        fg="#000000",
        font=("Arial", 10),
        wraplength=420,
        justify=LEFT,
    )
    text_label.pack(side=TOP, anchor=NW, padx=10, pady=5, fill=BOTH, expand=True)


# ==================Dynamic Combat Screen==================#
def show_combat_screen(enemy_type="goblin"):
    combat_frame = Frame(root, bg="#ffffff")
    combat_frame.pack(fill=BOTH, expand=True)

    arena_frame = Frame(combat_frame, bg="#ffffff")
    arena_frame.pack(fill=BOTH, expand=True)

    if enemy_type == "wizard":
        enemy_name = "Evil Wizard"
        enemy_img = wizard_img
    else:
        enemy_name = "Evil Goblin"
        enemy_img = goblin_img

    if enemy_img:
        enemy_label = Label(arena_frame, image=enemy_img, bg="#ffffff")
    else:
        enemy_label = Label(
            arena_frame,
            text=f"[ {enemy_name.upper()} ]",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg="red",
        )
    enemy_label.pack(side=TOP, anchor=NE, padx=40, pady=20)

    combat_box = Frame(
        combat_frame, bg="#333333", height=130, padx=12, pady=12
    )
    combat_box.pack_propagate(False)
    combat_box.pack(fill=X, side=BOTTOM)

    inner_hud = Frame(combat_box, bg="#ffffff", bd=2, relief="solid")
    inner_hud.pack(fill=BOTH, expand=True)

    status_label = Label(
        inner_hud,
        text=f"An {enemy_name} appeared!",
        bg="#ffffff",
        fg="black",
        font=("Arial", 10, "bold"),
    )
    status_label.pack(side=TOP, pady=(10, 5))

    btn_container = Frame(inner_hud, bg="#ffffff")
    btn_container.pack(side=BOTTOM, expand=True, pady=(0, 10))

    def end_combat():
        global current_round
        current_round += 1
        next_target = "victory" if current_round > MAX_ROUNDS else "options"
        animation_loading(combat_frame, next_screen=next_target)

    def attack_action():
        status_label.config(text=f"You defeated the {enemy_name}!")
        root.after(1000, end_combat)

    def magic_action():
        status_label.config(
            text=f"You cast Magic and vanquished the {enemy_name}!"
        )
        root.after(1000, end_combat)

    def run_action():
        end_combat()

    btn1 = Button(
        btn_container,
        text="Attack",
        bg="#e0e0e0",
        fg="black",
        font=("Arial", 9, "bold"),
        width=10,
        bd=2,
        relief="groove",
        command=attack_action,
    )
    btn1.pack(side=LEFT, padx=8)

    btn2 = Button(
        btn_container,
        text="Magic",
        bg="#e0e0e0",
        fg="black",
        font=("Arial", 9, "bold"),
        width=10,
        bd=2,
        relief="groove",
        command=magic_action,
    )
    btn2.pack(side=LEFT, padx=8)

    btn3 = Button(
        btn_container,
        text="Run",
        bg="#e0e0e0",
        fg="black",
        font=("Arial", 9, "bold"),
        width=10,
        bd=2,
        relief="groove",
        command=run_action,
    )
    btn3.pack(side=LEFT, padx=8)


# ==================Victory Screen==================#
def show_victory_screen():
    vic_frame = Frame(root, bg="#1e1e2e")
    vic_frame.pack(fill=BOTH, expand=True)

    vic_label = Label(
        vic_frame,
        text="VICTORY!\nYou completed all 3 rounds!",
        fg="gold",
        bg="#1e1e2e",
        font=("Arial", 20, "bold"),
        justify=CENTER,
    )
    vic_label.pack(expand=True)

    restart_btn = Button(
        vic_frame,
        text="Play Again",
        bg="#0B7480",
        fg="white",
        font=("Arial", 12, "bold"),
        padx=15,
        pady=5,
        command=lambda: reset_game(vic_frame),
    )
    restart_btn.pack(pady=(0, 80))


def reset_game(current_frame):
    global current_round
    current_round = 1
    current_frame.pack_forget()
    load_options_screen()


# ----STARTER SCREEN----#
top_frame = Frame(root)
top_frame.pack(fill=X)

bottom_frame = LabelFrame(root, text="Test")
bottom_frame.pack(fill=X, expand=True, padx=10, pady=10)

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