import json
from pathlib import Path
from models import Monster, Move

DATA_DIR = Path(__file__).parent / "data"

def load_json(filename):
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        return json.load(f)

MOVES = {key: Move(m["name"], m["power"]) for key, m in load_json("moves.json").items()}
MONSTER_DATA = load_json("monsters.json")

def create_monster(key):
    data = MONSTER_DATA[key]
    return Monster(
        data["name"],
        data["max_hp"],
        data["attack"],
        data["defense"],
        [MOVES[m] for m in data["moves"]],
    )