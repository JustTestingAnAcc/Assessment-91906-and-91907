from tkinter import *
from Game_Logic import GameState

root = Tk()
root.title("testing")
root.geometry("500x550")
root.resizable(False, False)

# Initialize Game Logic Instance
game = GameState(max_rounds=3)

# ========================== ASSET LOADING MAP ========================== #
assets = {}

def load_image(file_path):
    try:
        return PhotoImage(file=file_path)
    except Exception:
        return None

#makes it so that the images are loaded into the assets dictionary with their respective keys. If an image fails to load, it will return None instead of crashing the program.


assets["character"] = load_image("character.png")
assets["goblin"] = load_image("goblinNPC.png")
assets["wizard"] = load_image("wizardDialouge.png")
assets["sword_rock"] = load_image("SwordRock.png")
assets["undead_knight"] = load_image("character.png")
assets["golem"] = load_image("character.png")
assets["village"] = load_image("character.png")
assets["dwarf"] = load_image("character.png")
assets["broken_house"] = load_image("character.png")
assets["dolphin"] = load_image("character.png")
assets["boss"] = load_image("character.png")


# ========================== HUD DISPLAY ========================== #
def create_hud(parent_frame):
    hud = Frame(parent_frame, bg="#222222", height=30)
    hud.pack(fill=X, side=TOP)

    p = game.player
    sword_text = "" if p["has_sword"] else ""
    stats_text = (
        f"HP: {p['hp']}/{p['max_hp']}  |  Gold: {p['gold']} {sword_text}"
    )

    lbl = Label(
        hud,
        text=stats_text,
        bg="#222222",
        fg="white",
        font=("Arial", 9, "bold"),
    )
    lbl.pack(pady=5)

#

# ========================== LOADING SCREEN ========================== #
def animation_loading(current_frame, next_screen="options", event_data=None):
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
            if next_screen == "combat":
                show_combat_screen(event_data)
            elif next_screen == "victory":
                show_end_screen("VICTORY!", "You completed all 3 rounds!", "gold")
            elif next_screen == "game_over":
                show_end_screen("GAME OVER", "You perished in battle...", "red")
            else:
                load_options_screen()

    updt_prog()


# ========================== MAIN OPTIONS SCREEN ========================== #
def load_options_screen():
    if not game.is_player_alive():
        show_end_screen("GAME OVER", "You perished in battle...", "red")
        return

    if game.is_game_complete():
        show_end_screen("VICTORY!", "You completed all 3 rounds!", "gold")
        return

    game_screen = Frame(root, bg="#ffffff")
    game_screen.pack(fill=BOTH, expand=True)

    create_hud(game_screen)

    #This generates the title label and the option buttons for the current round. It also includes the "Scavenge" and "Rest" buttons as alternative actions.
    #Aswell as the function to disable all buttons once an option is selected, and then it calls the show_dialogue_screen function with the selected option.


    title_label = Label(
        game_screen,
        text=f"Round {game.current_round} / {game.max_rounds}: Choose where to go?",
        bg="#ffffff",
        font=("Arial", 13, "bold"),
    )
    title_label.pack(pady=10)

    cards_frame = Frame(game_screen, bg="#ffffff")
    cards_frame.pack(fill=BOTH, expand=True, padx=20, pady=5)
    cards_frame.columnconfigure((0, 1, 2), weight=1, uniform="card")
    cards_frame.rowconfigure(0, weight=1)

    options = game.get_round_options()
    option_buttons = []

    def disable_all_options(selected_option):
        for btn in option_buttons:
            btn.config(state=DISABLED)
        show_dialogue_screen(game_screen, selected_option)

    for col_index, option in enumerate(options):
        btn_text = f"Option {col_index + 1}\n({option['title']})"

        opt_btn = Button(
            cards_frame,
            text=btn_text,
            bg="#f0f0f0",
            font=("Arial", 10, "bold"),
            bd=2,
            relief="groove",
            command=lambda opt=option: disable_all_options(opt),
        )
        opt_btn.grid(row=0, column=col_index, padx=5, sticky="nsew")
        option_buttons.append(opt_btn)

    Alt_button = Frame(game_screen, bg="#ffffff")
    Alt_button.pack(fill=X, padx=20, pady=15)

    scavenge_btn = Button(
        Alt_button,
        text="Scavenge (+10 Gold)",
        bg="#e0e0e0",
        font=("Arial", 9, "bold"),
        command=lambda: disable_all_options({
            "title": "Scavenge",
            "is_combat": False,
            "dialogue": game.scavenge_gold(10),
            "asset_key": None
        }),
    )
    scavenge_btn.pack(side=LEFT)
    option_buttons.append(scavenge_btn)

    rest_btn = Button(
        Alt_button,
        text="Rest (+25 HP)",
        bg="#e0e0e0",
        font=("Arial", 9, "bold"),
        command=lambda: disable_all_options({
            "title": "Rest",
            "is_combat": False,
            "dialogue": game.rest_player(25),
            "asset_key": None
        }),
    )
    rest_btn.pack(side=RIGHT)
    option_buttons.append(rest_btn)


def start_game(): #this is the started function that is called when the "Start" button is pressed. It disables the start button, resets the game state, and transitions to the main game screen.
    button.config(state=DISABLED)
    game.reset_game()

    top_frame.pack_forget()
    bottom_frame.pack_forget()
    button.place_forget()

    game_frame = Frame(root, bg="#0B7480")
    game_frame.pack(fill=BOTH, expand=True)

    game_label = Label(
        game_frame,
        text="WIP+DEMO\n Not Finished",
        fg="yellow",
        bg="#0B7480",
        font=("Arial", 28, "bold"),
    )
    game_label.pack(expand=True)

    action_bar = Frame(game_frame, bg="#333333", pady=10)
    action_bar.pack(fill=X, side=BOTTOM)

    def explore_world():
        action_btn.config(state=DISABLED)
        animation_loading(game_frame)

    action_btn = Button(  #Action button that allows the player to explore the world. When clicked, it disables itself and triggers the loading animation before transitioning to the next game screen.
        action_bar,
        text="Explore World",
        font=("Arial", 11, "bold"),
        command=explore_world,
    )
    action_btn.pack(pady=5)


# ========================== DIALOGUE SCREEN ========================== #
def show_dialogue_screen(previous_screen, event_data): #This is just a dialogue screen that displays the event dialogue and any effects it has on the player. It also includes a button to continue to the next screen, which can be either combat or the next round of options.
    previous_screen.pack_forget()

    effect_text = game.apply_event_effects(event_data)
    dialogue_text = event_data["dialogue"] + effect_text

    dialouge_frame = Frame(root, bg="#ffffff")
    dialouge_frame.pack(fill=BOTH, expand=True)

    create_hud(dialouge_frame)

    scene_frame = Frame(dialouge_frame, bg="#f9f9f9")
    scene_frame.pack(fill=BOTH, expand=True)

    display_img = assets.get(event_data.get("asset_key"))
    if display_img:
        character_label = Label(scene_frame, image=display_img, bg="#f9f9f9")
    else:
        character_label = Label(
            scene_frame,
            text=f"[ {event_data['title'].upper()} ]",
            font=("Arial", 14, "bold"),
            bg="#f9f9f9",
            fg="#777777",
        )
    character_label.pack(expand=True)

    dialouge_box = Frame(dialouge_frame, bg="#333333", height=130, padx=10, pady=10) 
    dialouge_box.pack_propagate(False)
    dialouge_box.pack(fill=X, side=BOTTOM)

    bubble = Frame(dialouge_box, bg="#ffffff", bd=2, relief="solid")
    bubble.pack(fill=BOTH, expand=True)

    def advance_game(): 
        continue_btn.config(state=DISABLED)
        is_combat = event_data.get("is_combat", False)
        if not is_combat:
            game.advance_round()

        next_target = (
            "combat"
            if is_combat
            else ("victory" if game.is_game_complete() else "options")
        )
        animation_loading(
            dialouge_frame, next_screen=next_target, event_data=event_data
        )

    continue_btn = Button( #This lets user continue to the next screen after reading the dialogue. It checks if the event is a combat event or not, and then transitions to the appropriate next screen.
        bubble,
        text="Fight!" if event_data.get("is_combat") else "Continue >",
        bg="red" if event_data.get("is_combat") else "black",
        fg="white",
        font=("Arial", 9, "bold"),
        command=advance_game,
    )
    continue_btn.pack(side=BOTTOM, anchor=SE, padx=8, pady=5)

    text_label = Label(
        bubble,
        text=dialogue_text,
        bg="#ffffff",
        fg="#000000",
        font=("Arial", 9),
        wraplength=420,
        justify=LEFT,
    )
    text_label.pack(side=TOP, anchor=NW, padx=10, pady=5, fill=BOTH, expand=True)


# ========================== COMBAT SCREEN ========================== #
def show_combat_screen(event_data): 
    combat_frame = Frame(root, bg="#ffffff")
    combat_frame.pack(fill=BOTH, expand=True)

    create_hud(combat_frame) #What this does it creates a GUI/HUD screen for combat encounters. It displays the enemy's name, HP, and image, as well as a status label and buttons for the player to choose their combat actions (Attack, Magic, Run). The combat logic is handled through functions that calculate damage, update HP, and determine the outcome of the battle.

    arena_frame = Frame(combat_frame, bg="#ffffff")
    arena_frame.pack(fill=BOTH, expand=True)

    enemy_name = event_data.get("enemy_name", "Enemy")
    enemy_hp = [event_data.get("enemy_hp", 30)]
    enemy_atk = event_data.get("enemy_atk", 10)
    enemy_img = assets.get(event_data.get("asset_key"))

    if enemy_img:      #only Enemy/Mobs are displayed as images if they have an associated image in the assets dictionary. If not, a text label is used instead.
        enemy_label = Label(arena_frame, image=enemy_img, bg="#ffffff")
    else:
        enemy_label = Label(
            arena_frame,
            text=f"[ {enemy_name.upper()} ]",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg="red",
        )
    enemy_label.pack(side=TOP, anchor=NE, padx=40, pady=10)

    hp_display = Label(     #The health bar for the enemy is displayed as a label that updates dynamically based on the enemy's current HP. It shows the enemy's name and remaining HP, and is styled with a red font to indicate danger.
        arena_frame,
        text=f"{enemy_name} HP: {enemy_hp[0]}",
        font=("Arial", 11, "bold"),
        bg="#ffffff",
        fg="darkred",
    )
    hp_display.pack(side=TOP, anchor=NE, padx=40)

    combat_box = Frame(combat_frame, bg="#333333", height=130, padx=12, pady=12)
    combat_box.pack_propagate(False)
    combat_box.pack(fill=X, side=BOTTOM)

    inner_hud = Frame(combat_box, bg="#ffffff", bd=2, relief="solid")
    inner_hud.pack(fill=BOTH, expand=True)

    status_label = Label(
        inner_hud,
        text=f"A hostile {enemy_name} attacks!",
        bg="#ffffff",
        fg="black",
        font=("Arial", 9, "bold"),
    )
    status_label.pack(side=TOP, pady=(5, 0))

    btn_container = Frame(inner_hud, bg="#ffffff")
    btn_container.pack(side=BOTTOM, expand=True, pady=(0, 5))

    def disable_combat_actions():
        btn1.config(state=DISABLED)
        btn2.config(state=DISABLED)
        btn3.config(state=DISABLED)

    def enable_combat_actions():
        btn1.config(state=NORMAL)
        btn2.config(state=NORMAL)
        btn3.config(state=NORMAL)

    def enemy_turn():
        if enemy_hp[0] <= 0:
            status_label.config(text=f"You vanquished the {enemy_name}! (+20 Gold)")
            game.add_combat_reward(20)
            root.after(1200, finish_combat)
            return

        current_hp = game.receive_enemy_damage(enemy_atk)
        if not game.is_player_alive():
            status_label.config(text=f"The {enemy_name} dealt a lethal hit!")
            root.after(1200, lambda: animation_loading(combat_frame, "game_over"))
        else:
            status_label.config(
                text=f"Enemy dealt {enemy_atk} DMG to you! (Your HP: {current_hp})"
            )
            enable_combat_actions()

    def finish_combat():
        game.advance_round()
        next_target = "victory" if game.is_game_complete() else "options"
        animation_loading(combat_frame, next_screen=next_target)

    def attack_action():
        disable_combat_actions()
        dmg = game.calculate_attack_damage()
        enemy_hp[0] = max(0, enemy_hp[0] - dmg)
        hp_display.config(text=f"{enemy_name} HP: {enemy_hp[0]}")
        status_label.config(text=f"You struck the enemy for {dmg} DMG!")
        root.after(800, enemy_turn)

    def magic_action():
        disable_combat_actions()
        dmg = game.calculate_magic_damage()
        enemy_hp[0] = max(0, enemy_hp[0] - dmg)
        hp_display.config(text=f"{enemy_name} HP: {enemy_hp[0]}")
        status_label.config(text=f"You cast Magic for {dmg} DMG!")
        root.after(800, enemy_turn)

    def run_action():
        disable_combat_actions()
        status_label.config(text="You fled from battle!")
        root.after(800, finish_combat)

    btn1 = Button(
        btn_container,
        text="Attack",  #attack action
        bg="#e0e0e0",
        font=("Arial", 9, "bold"),
        width=8,
        command=attack_action,
    )
    btn1.pack(side=LEFT, padx=5)

    btn2 = Button(
        btn_container,
        text="Magic", #magic attack
        bg="#e0e0e0",
        font=("Arial", 9, "bold"),
        width=8,
        command=magic_action,
    )
    btn2.pack(side=LEFT, padx=5)

    btn3 = Button(
        btn_container,
        text="Run", #run away from combat
        bg="#e0e0e0",
        font=("Arial", 9, "bold"),
        width=8,
        command=run_action,
    )
    btn3.pack(side=LEFT, padx=5)


# ========================== GAME END SCREEN ========================== #
def show_end_screen(title, subtitle, color):
    end_frame = Frame(root, bg="#1e1e2e")
    end_frame.pack(fill=BOTH, expand=True)

    lbl = Label(
        end_frame,
        text=f"{title}\n{subtitle}",
        fg=color,
        bg="#1e1e2e",
        font=("Arial", 18, "bold"),
        justify=CENTER,
    )
    lbl.pack(expand=True)

    def restart_game():
        restart_btn.config(state=DISABLED)
        reset_game(end_frame)

    restart_btn = Button(
        end_frame,
        text="Play Again", #allows user to restart the game after winning or losing. It disables itself when clicked and calls the reset_game function to reset the game state and return to the main options screen.
        bg="#0B7480",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15,
        pady=5,
        command=restart_game,
    )
    restart_btn.pack(pady=(0, 60))


def reset_game(current_frame):
    game.reset_game()
    current_frame.pack_forget()
    load_options_screen()


# ---- STARTER SCREEN ----#
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