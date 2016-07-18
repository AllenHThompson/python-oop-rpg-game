import random
import time

class Character(object):

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        # if self.name == 'hero':
        #     self.health -= points
        #     self.health += self.armour
        # else:
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.name == 'Zombie' and self.health <= -10:
            print "%s is dead." % self.name
        elif self.name != 'Zombie' and self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armour = 0
        self.evade = 0

    def receive_damage(self, points):
        evade_points_1 = random.random() > 0.9
        evade_points_2 = random.random() > 0.85
        if self.evade == 2 and evade_points_1 == True:
            print "evade used"
        elif self.evade >= 4 and evade_points_2 == True:
            print "evade used"
        else:
            self.health -= points
            self.health += self.armour
            print "%s received %d damage." % (self.name, points)

        if self.name == 'Zombie' and self.health <= -10:
            print "%s is dead." % self.name
        elif self.name != 'Zombie' and self.health <= 0:
            print "%s is dead." % self.name

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        double_power = random.random() > 0.8
        if double_power == True:
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)
        time.sleep(1.5)

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 7

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 10
        self.power = 3
        self.coins = 8

    def receive_damage(self, points):
        self.health -= points
        recuperate = random.random() > 0.8
        if recuperate == True:
            self.health += 2
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 1
        self.power = 3
        self.coins = 10

    def receive_damage(self, points):
        shadow_damage = random.random() > 0.9
        if shadow_damage == True:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
        else:
            print "%s received no damage." % (self.name)
        if self.health <= 0:
            print "%s is dead." % self.name

class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.health = 5
        self.power = 3
        self.coins = 11

    def alive(self):
        return self.health > -10

class Dragon(Character):
    def __init__(self):
        self.name = 'Dragon'
        self.health = 10
        self.power = 3
        self.coins = 12

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        dragon_damage = random.random() > 0.5
        if dragon_damage == True:
            enemy.receive_damage(self.power * 10)
        else:
            enemy.receive_damage(self.power)
        time.sleep(1.5)

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            hero.coins += enemy.coins
            print "Hero has %s coins" % hero.coins
            return True
        else:
            print "YOU LOSE!"
            return False

class Evade(object):
    cost = 5
    name = 'Evade'
    def apply(self, character):
        character.evade += 2
        print "%s's evade amount increased to %d." % (character.name, character.evade)


class Armour(object):
    cost = 10
    name = "Armour"
    def apply(self, character):
        character.armour += 2
        print "%s's armour increased to %d." % (character.name, character.armour)

class SuperTonic(object):
    cost = 10
    name = 'SuperTonic'
    def apply(self, character):
        character.health += 10
        print "%s's health increased to %d." % (character.name, character.health)

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, character):
        character.power += 2
        print "%s's power increased to %d." % (character.name, character.power)

class Shopping(object):
    items = [Tonic, Sword, SuperTonic, Armour, Evade]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Dragon(), Zombie(), Goblin(), Wizard(), Medic(), Shadow()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
