import random

#
# No changes are required in this file.
#
 
class Character (object):
   
    def __init__ (self, name, hit_points, strength, dexterity, ability, small_image, large_image, attack1, attack2, attack3):
        '''
        Set the instance variables of name, hit_points, strength, and dexerity
        based upon the passed parameters.
        '''
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.dexterity = dexterity
        self.ability = ability
        self.small_image = small_image
        self.large_image = large_image
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3

    def bow_and_arrow (self, enemy):
        passive_chance = random.randint(0, 100)
        if passive_chance < 15:
            self.dexterity += random.randint(3, 7)
        total_dex = self.dexterity - 10 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if hit_attempt <= self.dexterity - 10:
            if enemy.ability == "Armor":
                damage = random.randrange(self.strength + 5, self.strength + 15)
                enemy.hit_points -= int(damage) * 0.8
                result = self.name + " used Bow and Arrow on " + enemy.name + " causing " + str(damage) + " damage."
            else:
                damage = random.randrange(self.strength + 5, self.strength + 15)
                enemy.hit_points -= damage
                result = self.name + " used Bow and Arrow on  " + enemy.name + " causing " + str(damage) + " damage."
        else:
            result = self.name + " missed " + enemy.name + "."

        return result

    def axe_blow (self, enemy):
        total_dex = self.dexterity - 15 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity - 15):
            damage = random.randrange(self.strength + 5, self.strength + 20)
            enemy.hit_points -= damage
            result = self.name + " used Axe Blow on  " + enemy.name + " causing " + str(damage) + " damage."
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def bite (self, enemy):
        total_dex = self.dexterity - 15 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity - 15):
            damage = random.randrange(self.strength + 5, self.strength + 20)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Bite on " + enemy.name + " causing " + str(damage) + " damage."
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def sword_slash (self, enemy):
        passive_chance = random.randint(0, 100)
        if passive_chance < 15:
            thing = random.randint(2, 6)
            enemy.dexterity -= thing
        total_dex = self.dexterity - 10 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity - 10):
            list = [self.strength + 5, self.strength + 15]
            damage = random.choice(list)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Sword Slash on " + enemy.name + " causing " + str(damage) + " damage. "
            if passive_chance < 15:
                result += enemy.name + "'s dexterity fell by " + str(thing)
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def fireball (self, enemy):
        total_dex = self.dexterity - 10 + enemy.dexterity
        hit_attempt = random.randint(0, total_dex)
        if (hit_attempt <= self.dexterity - 10):
            list = [self.strength + 25, self.strength + 40]
            damage = random.choice(list)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Fireball on " + enemy.name + " causing " + str(damage) + " damage."
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def war_cry (self):
        increase_strength = random.randint(10, 15)
        self.strength += increase_strength
        result = "Orc's strength increased by " + str(num)

        return result

    def club_smash (self, enemy):
        total_dex = self.dexterity + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity):
            list = [self.strength - 5, self.strength]
            damage = random.choice(list)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Club Smash on " + enemy.name + " causing " + str(damage) + " damage."
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def back_stab (self, enemy):
        passive_chance = random.randint(0, 100)
        if passive_chance < 15:
            thing = random.randint(3, 7)
            self.dexterity += thing
        total_dex = self.dexterity + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity):
            damage = random.randrange(self.strength - 5, self.strength)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Back Stab on " + enemy.name + " causing " + str(damage) + " damage. "
            if passive_chance < 15:
                result += self.name + "'s dexterity was raised by " + str(thing)
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def hammer_swing (self, enemy):
        total_dex = self.dexterity + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity):
            damage = random.randrange(self.strength - 5, self.strength)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Hammer Swing on " + enemy.name + " causing " + str(damage) + " damage."
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def stab (self, enemy):
        passive_chance = random.randint(0, 100)
        if passive_chance < 15:
            thing = random.randint(2, 6)
            enemy.dexterity -= thing
        total_dex = self.dexterity + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity):
            list = [self.strength - 5, self.strength]
            damage = random.choice(list)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Stab on " + enemy.name + " causing " + str(damage) + " damage. "
            if passive_chance < 15:
                result += enemy.name + "'s dexterity fell by " + str(thing)
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def arcane_blast (self, enemy):
        total_dex = self.dexterity + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity):
            thing = self.strength + 30
            thing2 = self.strength + 15
            list = [thing, thing2]
            damage = random.choice(list)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Arcane Blast on " + enemy.name + " causing " + str(damage) + " damage."
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def sneak_attack (self, enemy):
        passive_chance = random.randint(0, 100)
        if passive_chance < 15:
            thing = random.randint(3, 7)
            self.dexterity += thing
        total_dex = self.dexterity + 10 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity + 10):
            damage = random.randrange(self.strength - 5, self.strength)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Sneak Attack on " + enemy.name + " causing " + str(damage) + " damage."
            if passive_chance < 15:
                result += self.name + "'s dexterity was raised by " + str(thing)
        else:
            result = self.name + " misses " + enemy.name + "."
        chance = random.randint(0, 100)
        if chance < 25:
            num = random.randint(3, 7)
            self.dexterity += num
            result += ". Elf's dexterity was raised by " + str(num)

        return result

    def crippling_blow (self, enemy):
        total_dex = self.dexterity - 5 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity - 5):
            damage = random.randrange(self.strength + 10, self.strength)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Crippling Blow on " + enemy.name + " causing " + str(damage) + " damage."
            chance = random.randint(0, 100)
            if chance < 25:
                num = random.randint(3, 7)
                enemy.dexterity -= num
                result += ". " + enemy.name + "'s dexterity fell by " + str(num)
        else:
            result = self.name + " misses " + enemy.name + "."

        return result

    def electrify (self, enemy):
        total_dex = self.dexterity - 10 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.dexterity - 10):
            list = [self.strength + 35, self.strength+ 20]
            damage = random.choice(list)
            if enemy.ability == "Armor":
                damage *= 0.8
                enemy.hit_points -= damage
            else:
                enemy.hit_points -= damage
            result = self.name + " used Electrify on " + enemy.name + " causing " + str(damage) + " damage."
            chance = random.randint(0, 100)
            if chance < 25:
                num = random.randint(3, 7)
                enemy.strength -= num
                result += ". " + enemy.name + "'s strength fell by " + str(num)
        else:
            result = self.name + " misses " + enemy.name + "."


        return result

    def headbutt (self, enemy):
        total_dex = self.dexterity - 10 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        damage_chance = random.randint(0,100)
        if damage_chance >= 50:
            if hit_attempt <= self.dexterity - 10:
                list = [self.strength - 5, self.strength]
                damage = random.choice(list)
                if enemy.ability == "Armor":
                    damage *= 0.8
                    enemy.hit_points -= damage
                else:
                    enemy.hit_points -= damage
                result = self.name + " used Headbutt on " + enemy.name + " causing " + str(damage) + " damage."
            else:
                result = self.name + " misses " + enemy.name + "."
        elif damage_chance < 50:
            if hit_attempt <= self.dexterity - 10:
                list = [self.strength + 30, self.strength + 20]
                damage = random.choice(list)
                enemy.hit_points -= damage
                result = self.name + " used Headbutt on " + enemy.name + " causing " + str(damage) + " damage."
            else:
                result = self.name + " misses " + enemy.name + "."

        return result

    def shield_bash(self, enemy):
        total_dex = self.dexterity - 10 + enemy.dexterity
        hit_attempt = random.randrange(0, total_dex)
        damage_chance = random.randint(0, 100)
        if damage_chance >= 50:
            if hit_attempt <= self.dexterity - 10:
                list = [self.strength - 5, self.strength]
                damage = random.choice(list)
                if enemy.ability == "Armor":
                    damage *= 0.8
                    enemy.hit_points -= damage
                else:
                    enemy.hit_points -= damage
                result = self.name + " used Shield Bash on " + enemy.name + " causing " + str(damage) + " damage."
            else:
                result = self.name + " misses " + enemy.name + "."
        elif damage_chance < 50:
            if hit_attempt <= self.dexterity - 10:
                list = [self.strength + 30, self.strength + 20]
                damage = random.choice(list)
                enemy.hit_points -= damage
                result = self.name + " used Shield Bash on " + enemy.name + " causing " + str(damage) + " damage."
            else:
                result = self.name + " misses " + enemy.name + "."

        return result


    def die (self):
        ''' Prints a death message. '''
        print (self.name + ": Ahhhhh.. too much damage!  I have died.")

    def __str__ (self):
        ''' Prints the name, hit points, strength, and dexterity of the object. '''
        return self.name + "; HP: " + str(self.hit_points) + "; Strength: " + str(self.strength) + "; Dexterity: " + str(self.dexterity)

class CharacterList (object):
    def __init__ (self, file_name):
        '''
        This method intializes a new CharacterList object by loading
        a list of Characters from file_name.
        The file is in comma, separated format.  The fields of the file include:
            <Name>,<Hit Points>,<Strength>,<Dexterity>
        '''
        self.character_list = []

        text_file = open(file_name,"r")

        for line in text_file:
            line = line.strip()
            my_fields = line.split(", ")
            character = Character (my_fields[0], int(my_fields[1]), int(my_fields[2]), int(my_fields[3]), my_fields[4], my_fields[5], my_fields[6], my_fields[7], my_fields[8], my_fields[9])
            self.character_list.append(character)
    
    def print_list (self):
        ''' 
        Prints the list of characters_base, using the __str__ function of Character object.
        '''
        for i in range (len(self.character_list)):
            print (str(i) +": " + str(self.character_list[i]))        
    
    def get_and_remove_character (self, i):
        ''' 
        Gets and returns the "ith" Character from the list, then removes the 
        character from the list.  (Doing so prevents the user and computer from 
        using the same character.
        '''
        ch = self.character_list[i]
        self.character_list.remove(self.character_list[i])
        return ch
    
    def get_random_character (self):
        ''' Gets and returns a random character from the list (for the computer). '''
        return random.choice(self.character_list)
    
    def get_number_of_characters (self):
        ''' Returns the number of characters_base in the list. '''
        return len(self.character_list)

