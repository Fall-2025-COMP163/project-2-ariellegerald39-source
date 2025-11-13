"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Arielle Gerald
Date: 11/14/2025

AI Usage: This project was completed with full assistance from Chat GPT. 
AI was used to generate and refine all class implementations and method definitions.
I have reviewed and studied every part of the implementation to ensure understanding.

Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
"""
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    # Base class that defines the shared structure and behavior for all characters.
    # Every subclass will inherit from this one.
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
         # Basic setup for a character’s name, health, and combat stats
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        """Initialize basic character attributes"""
       
        
        
    def attack(self, target):
        # Standard attack that simply uses the strength stat for damage
        damage = self.strength
        print(self.name + " attacks " + target.name + " for " + str(damage) + " damage!")
        target.take_damage(damage)
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
       
        
    def take_damage(self, damage):
         # Subtract health and make sure it doesn’t drop below zero
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        print(self.name + " now has " + str(self.health) + " HP.")
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        
        
        
    def display_stats(self):
        # Prints current stats for quick debugging or battle output
        print("Name:", self.name)
        print("Health:", self.health)
        print("Strength:", self.strength)
        print("Magic:", self.magic)
        """
        Prints the character's current stats in a nice format.
        """
        
        

class Player(Character):
    # Extension of Character that adds leveling, experience, and weapon support.
    # Used as a parent for specific player archetypes (Warrior, Mage, Rogue).
    def __init__(self, name, character_class, health, strength, magic):
        # Initialize inherited attributes first, then add player-specific fields
        Character.__init__(self, name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.weapon = None # Starts unarmed until a weapon is equipped
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """

    """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
       
        
    def display_stats(self):
        # Adds player-specific info like class, level, and weapon to the base stats
        print("=== " + self.character_class + " ===")
        Character.display_stats(self)
        print("Level:", self.level)
        print("Experience:", self.experience)

        # If a weapon is equipped, show it, otherwise indicate unarmed status
        if self.weapon is not None:
            print("Equipped Weapon:", self.weapon.name, "(+" + str(self.weapon.damage_bonus) + ")")
        else:
            print("No weapon equipped.")

    def equip_weapon(self, weapon):
        # Assign a weapon to the player and confirm the change
        """Equip a weapon."""
        self.weapon = weapon
        print(self.name + " equipped " + weapon.name + "!")
        
    def attack(self, target):
        # Attack calculation that includes any weapon bonus
        """Attack that includes weapon bonus if equipped."""
        damage = self.strength
        if self.weapon is not None:
            damage = damage + self.weapon.damage_bonus
        print(self.name + " attacks " + target.name + " for " + str(damage) + " damage!")
        target.take_damage(damage)
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        
        

class Warrior(Player):
    # Heavy fighter that specializes in physical attacks.
    # Trades magic ability for raw power and endurance.
    def __init__(self, name):
        # Set Warrior’s default stats (high HP, high strength, low magic)
        Player.__init__(self, name, "Warrior", 120, 15, 5)

    def attack(self, target):
        # Slightly stronger than the normal player attack
        damage = self.strength + 5
        print(self.name + " swings at " + target.name + " for " + str(damage) + " damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        # A signature Warrior move that doubles their strength for one hit
        damage = self.strength * 2
        print(self.name + " uses Power Strike on " + target.name + " for " + str(damage) + " damage!")
        target.take_damage(damage)
    
"""
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
"""
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        
        
    
"""
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
       
        
        
    
"""
        Special warrior ability - a powerful attack that does extra damage.
        """
       
        

class Mage(Player):
    # A fragile but powerful magic user who focuses on spell attacks.
    
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        

    def __init__(self, name):
        # Mages have lower HP and strength but excel in magic
        Player.__init__(self, name, "Mage", 80, 8, 20)     
        
    def attack(self, target):
         # Replace physical damage with magic-based attacks
        damage = self.magic
        print(self.name + " casts a spell at " + target.name + " for " + str(damage) + " damage!")
        target.take_damage(damage)
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
       
        
        
    def fireball(self, target):
        # Stronger version of the attack, doubles the magic output
        damage = self.magic * 2
        print(self.name + " casts Fireball on " + target.name + " for " + str(damage) + " damage!")
        target.take_damage(damage)
        """
        Special mage ability - a powerful magical attack.
        """
        
        

class Rogue(Player):
    # Crafty and agile fighter who relies on speed and precision.
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        # Rogues have moderate stats
        Player.__init__(self, name, "Rogue", 90, 12, 10)
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        
        
        
    def attack(self, target):
        # Standard quick attack, doesn’t hit as hard as a warrior’s swing
        damage = self.strength
        print(self.name + " swiftly strikes " + target.name + " for " + str(damage) + " damage!")
        target.take_damage(damage)
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        
        
        
    def sneak_attack(self, target):
        # A hard hit thats double the normal damage
        damage = self.strength * 2
        print(self.name + " performs a Sneak Attack on " + target.name + " for " + str(damage) + " damage!")
        target.take_damage(damage)
"""
        Special rogue ability - guaranteed critical hit.
"""
        
        

class Weapon:
    # Represents a piece of equipment that increases attack power.
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
         # Save weapon name and its damage boost value
        self.name = name
        self.damage_bonus = damage_bonus
        """
        Create a weapon with a name and damage bonus.
        """
       
        
        
    def display_info(self):
        # Output weapon stats for the player or debugging
        print("Weapon:", self.name, "(+" + str(self.damage_bonus) + " Damage Bonus)")
        """
        Display information about this weapon.
        """
        

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
