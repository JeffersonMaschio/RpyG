# monstros, moves

import json
from pathlib import Path

class Monster:
    def __init__(self, name: str, max_hp: int, damage: int, defense: int, moves: list[Move]):
        self.name: str = name
        self.hp: int = max_hp
        self.max_hp: int = max_hp
        self.damage: int = damage
        self.defense: int = defense
        self.moves: list[Move] = moves

    def take_damage(self, amount: int):
        self.max_hp = self.max_hp - amount

class Hero:
    def __init__(self, name: str, max_hp: int, damage: int, defense: int, moves: list[Move]):
        self.name: str = name
        self.hp: int = max_hp
        self.max_hp: int = max_hp
        self.damage: int = damage
        self.defense: int = defense
        self.moves: list[Move] = moves

    def take_damage(self, amount: int):
        self.max_hp = self.max_hp - amount

    def use_move(self, move, target):
        if move.type == "heal":
            self.heal(move.value)
        else:
            target.take_damage(move.value)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

class Move:
    def __init__(self, name: str, type: str, damage: int):
        self.name: str = name
        self.type: str = type
        self.damage: int = damage
    
    def __repr__(self) -> str: #tipo toString() do java
        return f"Move({self.name}, {self.type}, {self.damage})"

#------------------------------------------------------------------------

DATA_DIR = Path(__file__).parent / "data"

def load_json(filename):
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        return json.load(f)

MOVES = {key: Move(m["name"], m["type"], m["damage"]) for key, m in load_json("moves.json").items()}
MONSTER_DATA = load_json("monsters.json")
HEROS_DATA = load_json("heros.json")

def create_monster(key: str) -> Monster:
    data = MONSTER_DATA[key]
    return Monster(
        data["name"],
        data["max_hp"],
        data["power"],
        data["defense"],
        [MOVES[m] for m in data["moves"]],
    )

def create_hero(key: str) -> Hero:
    data = HEROS_DATA[key]
    return Hero(
        data["name"],
        data["max_hp"],
        data["power"],
        data["defense"],
        [MOVES[m] for m in data["moves"]],
    )
