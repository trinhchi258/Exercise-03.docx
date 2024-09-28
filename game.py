import random
class Character:
    def __init__(self, name, health, attack_power, defence):
        self.name = name
        self.health = health
        self.attack_power = attack_power  
        self.defence = defence
    def attack(self, target):
        damage = max(0, self.attack_power - target.defence)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0 
    def is_alive(self):
        return self.health > 0
class Hero(Character):
    def special_attack(self, target):
        pass
class Warrior(Hero):
    def special_attack(self, target):
        damage = self.attack_power * 2 
        print(f"{self.name} special attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
class Mage(Hero):
    def special_attack(self, target):
        damage = self.attack_power * 1.5  
        print(f"{self.name} casts a powerful spell on {target.name} for {damage:.1f} damage!")
        target.take_damage(damage)
class Monster(Character):
    def roar(self):
        pass
class Orc(Monster):
    def roar(self):
        print(f"The Orc lets out a terrifying roar! {self.name} is ready to fight.")
class Dragon(Monster):
    def roar(self):
        print(f"The Dragon breathes fire as it roars! {self.name} is preparing to attack.")

# Mô phỏng trận chiến
def battle(hero, monster):
    print(f"--- Battle Start: {hero.name} vs {monster.name} ---")
    monster.roar()
    while hero.is_alive() and monster.is_alive():
        if random.choice([True, False]):  
            hero.attack(monster)
        else:
            hero.special_attack(monster)

        if not monster.is_alive():
            print(f"{monster.name} has been defeated!")
            break

        # Lượt của quái vật
        monster.attack(hero)
        if not hero.is_alive():
            print(f"{hero.name} has been defeated!")
            break

    print(f"--- Battle End: {hero.name} vs {monster.name} ---")

# Tạo một anh hùng Warrior và một quái vật Dragon
hero_warrior = Warrior(name="Conan", health=100, attack_power=20, defence=5)
monster_dragon = Dragon(name="Smaug", health=120, attack_power=25, defence=10)

# Bắt đầu trận chiến
battle(hero_warrior, monster_dragon)



