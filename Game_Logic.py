class GameState: #This isolates the game logic from the GUI, allowing for easier testing and maintenance. It manages player stats, combat calculations, round progression, and event effects without any direct interaction with the GUI components.

    def __init__(self, max_rounds=3):
        self.max_rounds = max_rounds
        self.reset_game()

    def reset_game(self):
        self.current_round = 1
        self.player = {
            "hp": 100,
            "max_hp": 100,
            "gold": 20,
            "has_sword": False,
            "atk_power": 15,
        }

    # ================= STAT HELPERS ================= #
    def rest_player(self, amount=25):  #Adds/Recovers HP to the player, ensuring it does not exceed max HP.
        self.player["hp"] = min(
            self.player["max_hp"], self.player["hp"] + amount
        )
        return f"You rested and recovered {amount} HP."

    def scavenge_gold(self, amount=10): #Just a reward for the player. 
        self.player["gold"] += amount
        return f"You scavenged around and found {amount} Gold!"

    # ================= COMBAT MATH ================= #
    def calculate_attack_damage(self):
        return self.player["atk_power"]

    def calculate_magic_damage(self):
        return 25

    def receive_enemy_damage(self, enemy_atk):
        self.player["hp"] -= enemy_atk
        if self.player["hp"] < 0:
            self.player["hp"] = 0
        return self.player["hp"]

    def add_combat_reward(self, gold_amount=20):
        self.player["gold"] += gold_amount

    def is_player_alive(self):
        return self.player["hp"] > 0

    # ================= ROUND PROGRESSION ================= #
    def advance_round(self):
        self.current_round += 1

    def is_game_complete(self):
        return self.current_round > self.max_rounds

    def apply_event_effects(self, event_data):
        """Modifies player stats based on non-combat dialogue events."""
        event_type = event_data.get("event_type")

        if event_type == "sword_rock" and not self.player["has_sword"]:
            self.player["has_sword"] = True
            self.player["atk_power"] += 15
            return "\n( You pulled the Magic Sword! +15 ATK )"
        elif event_type == "village":
            self.rest_player(30)
        elif event_type == "dwarf":
            self.player["atk_power"] += 10
        elif event_type == "broken_house":
            self.player["gold"] += 50

        return ""

    # ================= ROUND DEFINITIONS ================= #
    def get_round_options(self):
        """Returns non-GUI round data keyed by round number."""
        round_data = {
            1: [
                {
                    "title": "Cave",
                    "is_combat": True,
                    "enemy_name": "Cave Goblin",
                    "enemy_hp": 80,
                    "enemy_atk": 10,
                    "asset_key": "goblin",
                    "dialogue": "You enter the dark cave. An Evil Goblin jumps out from the shadows!",
                },
                {
                    "title": "Forest",
                    "is_combat": True,
                    "enemy_name": "Dark Wizard",
                    "enemy_hp": 90,
                    "enemy_atk": 15,
                    "asset_key": "wizard",
                    "dialogue": "You walk into the enchanted forest. An Evil Wizard blocks your path!",
                },
                {
                    "title": "Plains",
                    "is_combat": False,
                    "event_type": "sword_rock",
                    "asset_key": "sword_rock",
                    "dialogue": "You stumble upon an ancient magical sword deeply embedded in a rock!",
                },
            ],
            2: [
                {
                    "title": "Crypt",
                    "is_combat": True,
                    "enemy_name": "Undead Knight",
                    "enemy_hp": 125,
                    "enemy_atk": 18,
                    "asset_key": "undead_knight",
                    "dialogue": "You step into the ancient crypt. An Undead Knight draws its sword!",
                },
                {
                    "title": "Mountain",
                    "is_combat": True,
                    "enemy_name": "Stone Golem",
                    "enemy_hp": 180,
                    "enemy_atk": 12,
                    "asset_key": "golem",
                    "dialogue": "The earth shakes as a Wandering Golem forms right in front of you!",
                },
                {
                    "title": "Village",
                    "is_combat": False,
                    "event_type": "village",
                    "asset_key": "village",
                    "dialogue": "You visit the village elder. She heals 30 HP for your journey!",
                },
            ],
            3: [
                {
                    "title": "Mines",
                    "is_combat": False,
                    "event_type": "dwarf",
                    "asset_key": "dwarf",
                    "dialogue": "A friendly Dwarf Merchant sharpens your weapon! (+10 Attack Power)",
                },
                {
                    "title": "Ruins",
                    "is_combat": False,
                    "event_type": "broken_house",
                    "asset_key": "broken_house",
                    "dialogue": "You scavenge a ruined house and find a pouch containing 50 Gold!",
                },
                {
                    "title": "Lake",
                    "is_combat": True,
                    "enemy_name": "Bubbles the Boss",
                    "enemy_hp": 230,
                    "enemy_atk": 23,
                    "asset_key": "dolphin",
                    "dialogue": "Bubbles the Dolphin turns evil! Prepare for the final boss battle!",
                },
            ],
        }
        return round_data.get(self.current_round, [])