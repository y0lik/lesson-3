# class Student:
#     id = 0
#
#     def __init__(self, name, age, edu):
#         self.name = name
#         self.age = age
#         self.edu = edu
#         self.id = Student.id
#         Student.id += 1
#
#     def info(self):
#         print(f"\nStudent: \nID:{self.id} "
#               f"\nName: {self.name}\nAge: {self.age}"
#               f"\nEdu: {self.edu}")
#
#
# s1 = Student("Alex", 20, "PoliteH")
# s2 = Student("Name2", 32, "k")
# s3 = Student("Asr", 10, "Poli")
# s4 = Student("Zx", 30, "Polite")
#
# s1.info()
# s2.info()
# s3.info()
# s4.info()
import random

class_group = ["Knight", "Berserk", "Archer", "Mage"]
list_stage = {
    -1: 'attack',
    0: 'protection',
    1: 'parry'
}


class Hero:
    def __init__(self, name, group, hp, armor, damage):
        self.name = name
        self.group = group
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def action(self):
        return input("Choose action: \n1. Attack\n2. Protection\n3. Parry\nEnter action: ")

    def attack(self, enemy):
        if enemy.stage == list_stage.get(-1):
            pass
        elif enemy.stage == list_stage.get(0):
            enemy.hp = enemy.hp - self.damage + enemy.armor
        elif enemy.stage == list_stage.get(1):
            pass


class Orc:
    def __init__(self, name, group, hp, armor, damage):
        self.name = name
        self.group = group
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.stage = 0

    def attack(self, enemy):
        if enemy.stage == list_stage.get(-1):
            pass
        elif enemy.stage == list_stage.get(0):
            enemy.hp = enemy.hp - self.damage + enemy.armor
        elif enemy.stage == list_stage.get(1):
            pass


class Arena:

    def battle(self, hero, orc):
        print("Battle Start:")
        while hero.hp > 0 and orc.hp > 0:
            print("Hero: ", hero.name, hero.group, hero.hp, hero.armor, hero.damage)
            print("Orc: ", orc.name, orc.group, orc.hp, orc.armor, orc.damage)
            action_bot = random.randint(-1, 1)
            turn = random.randint(0, 1)
            if turn > 0:
                action = hero.action()
                if action == 1:
                    hero.attack(orc)
                elif action == 2:
                    if orc.stage == -1:
                        hero.hp = hero.hp - orc.damage + hero.armor
                    else:
                        print("Nobody attack")
                elif action == 3:
                    if orc.stage == -1:
                        orc.hp = hero.hp - orc.damage + hero.armor * 2
                    else:
                        print("Nobody attack")
            elif turn < 0:
                if action_bot == 1:
                    orc.attack(hero)
                elif action_bot == 2:
                    if action == -1:
                        orc.hp = orc.hp - hero.damage + orc.armor
                    else:
                        print("Nobody attack")
                elif action_bot == 3:
                    if action == -1:
                        orc.hp = orc.hp - hero.damage + orc.armor * 2
                    else:
                        print("Nobody attack")


hero = Hero("Arthur", 0, 100, 5, 10)
orc1 = Orc("Orc1", 1, 125, 2, 12)
arena = Arena()
arena.battle(hero, orc1)
