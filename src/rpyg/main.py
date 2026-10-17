#loop principal

from .models import create_monster, create_hero


hero = create_hero("warrior")
def run():
    slime = create_monster("slime")
    print(slime.name, slime.max_hp)


    print(hero.name, hero.max_hp)
    slime.take_damage(5)
    print(slime.name, slime.max_hp)
    hero.take_damage(10)
    print(hero.name, hero.max_hp)



if __name__ == "__main__":
    run()