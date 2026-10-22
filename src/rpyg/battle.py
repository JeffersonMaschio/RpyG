#regras e turnos

#make conditions for each selected moves in a function

from .models import Hero, Monster

def checkSpeed(hero: Hero, monster: Monster, rounds: int = 10) -> list:
    if hero.speed >= monster.speed:   # empate: o herói começa
        first, second = hero, monster
    else:
        first, second = monster, hero

    queue = [first, second] * rounds  # [A, B, A, B, ...]
    print([c.name for c in queue])    # imprime nomes, não o repr dos objetos
    return queue
