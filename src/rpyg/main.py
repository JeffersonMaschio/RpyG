#loop principal
from time import sleep

from .models import create_monster, create_hero
from .battle import checkSpeed

hero = create_hero("paladin")
slime = create_monster("slime")

def run():
    checkSpeed(hero,slime)
    print("a slime apear")
    sleep(0.5)
    slime.show_stats()
    print()
    hero.show_stats()
    print(hero.moves)
    
if __name__ == "__main__":
    run()