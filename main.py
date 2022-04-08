class_group = ["Knight", "Berserk", "Archer", "Magic"]

class Hero:
    def __init__(self, name, group, hp, damage, armor):
        self.name = name
        self.group = group
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def action(self):
        print("Choose action: \n1. Attack \n2. Protection\n3. Parry")
class Orc:
    def __init__(self, name, group, hp, damage, armor):
        self.name = name
        self.group = group
        self.hp = hp
        self.armor = armor
        self.damage = damage

class Arena:
    def battle(self, hero, orc):
        print("Battle Start:")

hero = Hero("Arthur", 0, 100, 5, 10)
orc1 = Orc("Arthur", 1, 125, 2, 12)