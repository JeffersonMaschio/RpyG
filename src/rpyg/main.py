#loop principal
from time import sleep

from .models import create_monster, create_hero

hero = create_hero("paladin")
slime = create_monster("slime")

def run():
    print("a slime apear")
    sleep(0.5)
    slime.show_stats()
    print()
    hero.show_stats()
    print(hero.moves)
    move_choose = input("choose move:")
    if move_choose == "simple_attack":
        slime.take_damage(10)
        slime.show_stats()

if __name__ == "__main__":
    run()