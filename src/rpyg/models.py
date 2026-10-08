# monstros, moves

class Monster:
    def __init__(self, name, max_hp, damage):
        self.name = name   # guarda o nome DESTE monstro
        self.max_hp = max_hp       # guarda o HP DESTE monstro
        self.damage = damage

    def take_damage(self, amount):
        self.max_hp = self.max_hp - amount   # mexe no HP DESTE monstro

class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage