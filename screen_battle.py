import tkinter
import random

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_Battle, self).__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets for the battle page.
        '''
        self.font = ("Apple Chancery", 24)
        self.font2 = ("SignPainter", 70)

        self.attack_label1 = tkinter.Label(text="")
        self.attack_label2 = tkinter.Label(text="")


        self.atk1 = tkinter.Button(self, text = self.player1.attack1, command=self.attack_clicked)
        self.atk1.grid(row = 7, column = 0)
        self.atk2 = tkinter.Button(self, text = self.player1.attack2, command=self.attack_clicked)
        self.atk2.grid(row = 8, column = 0)
        self.atk3 = tkinter.Button(self, text=self.player1.attack3, command = self.attack_clicked)
        self.atk3.grid(row = 7, column = 2)

        self.end = tkinter.Label(self, text = "")
        self.end.grid(row = 3, column = 1)

        tkinter.Label(self, text = "You", font=self.font).grid(row = 2, column = 0)

        tkinter.Label(self, text = "Computer",font=self.font).grid(row = 2, column = 2)

        imageLarge = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label(self, image=imageLarge, )
        w.photo = imageLarge
        w.grid(row = 4, column=0, sticky=tkinter.N)

        tkinter.Label(self, text="V.S", font=self.font2).grid(row=4, column=1)

        imageLarge2 = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        x = tkinter.Label(self, image=imageLarge2, )
        x.photo = imageLarge2
        x.grid(row = 4, column=2, sticky=tkinter.N)

        self.you = tkinter.Label(self, text = str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP")
        self.you.grid(row = 6, column = 0)

        self.enemy = tkinter.Label(self, text = str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP")
        self.enemy.grid(row = 6, column = 2)
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and the computer.
            2) Updates the labels on the top right with the result of the attacks.
            3) Determines if there is a victor.
            4) If there is a victor, removes that Attack button and replaces it with an Exit button.
        '''


        self.attack_label1.destroy()
        self.attack_label2.destroy()

        ability_chance = random.randint(1, 2)

        if self.player1.name == "Orc":
            if ability_chance == 1:

                if self.player1.attack1 == "Club Smash":
                    a1 = self.player1.club_smash(self.player2)

                if self.player1.attack2 == "Bite":
                    a1 = self.player1.bite(self.player2)

                if self.player1.attack3 == "War Cry":
                    a1 = self.player1.war_cry(self)
            else:
                num = random.randint(5, 15)
                self.player1.strength += num
                a1 = "Orc fell asleep for one turn because of his exhaustion, but his attack was raised by " + str(num) + "!"

        if self.player1.name == "Elf":
            if ability_chance == 1:
                num = random.randint(5, 15)
                self.player1.dexterity += num

                if self.player1.attack3 == "Sneak Attack":
                    a1 = self.player1.sneak_attack(self.player2)

                if self.player1.attack2 == "Bow and Arrow":
                    a1 = self.player1.bow_and_arrow(self.player2)

                if self.player1.attack1 == "Back Stab":
                    a1 = self.player1.back_stab(self.player2)

                a1 += ". Elf's dexterity was raised by " + str(num) + "because of his Super Speed ability!"

            else:
                if self.player1.attack3 == "Sneak Attack":
                    a1 = self.player1.sneak_attack(self.player2)

                if self.player1.attack2 == "Bow and Arrow":
                    a1 = self.player1.bow_and_arrow(self.player2)

                if self.player1.attack1 == "Back Stab":
                    a1 = self.player1.back_stab(self.player2)


        if self.player1.attack3 == "Headbutt":
            a1 = self.player1.headbutt(self.player2)

        if self.player1.attack3 == "Shield Bash":
            a1 = self.player1.shield_bash(self.player2)

        if self.player1.attack3 == "Electrify":
            a1 = self.player1.electrify(self.player2)

        if self.player1.attack2 == "Axe Blow":
            a1 = self.player1.axe_blow(self.player2)

        if self.player1.attack2 == "Sword Slash":
            a1 = self.player1.sword_slash(self.player2)

        if self.player1.attack2 == "Fireball":
            a1 = self.player1.fireball(self.player2)

        if self.player1.attack1 == "Hammer Swing":
            a1 = self.player1.hammer_swing(self.player2)

        if self.player1.attack1 == "Stab":
            a1 = self.player1.stab(self.player2)

        if self.player1.attack1 == "Arcane Blast":
            a1 = self.player1.arcane_blast(self.player2)



        enemy_attack = random.randint(0, 2)

        if self.player2.name == "Orc":

            if enemy_attack == 0:
                a2 = self.player2.club_smash(self.player1)
            elif enemy_attack == 1:
                a2 = self.player2.bite(self.player1)
            elif enemy_attack == 2:
                a2 = self.player2.war_cry(self.player1)

        elif self.player2.name == "Elf":

            if enemy_attack == 0:
                a2 = self.player2.back_stab(self.player1)
            elif enemy_attack == 1:
                a2 = self.player2.bow_and_arrow(self.player1)
            elif enemy_attack == 2:
                a2 = self.player2.sneak_attack(self.player1)

        elif self.player2.name == "Dwarf":

            if enemy_attack == 0:
                a2 = self.player2.hammer_swing(self.player1)
            elif enemy_attack == 1:
                a2 = self.player2.axe_blow(self.player1)
            elif enemy_attack == 2:
                a2 = self.player2.headbutt(self.player1)

        elif self.player2.name == "Dark Knight":

            if enemy_attack == 0:
                a2 = self.player2.stab(self.player1)
            elif enemy_attack == 1:
                a2 = self.player2.sword_slash(self.player1)
            elif enemy_attack == 2:
                a2 = self.player2.shield_bash(self.player1)

        elif self.player2.name == "Wizard":

            if enemy_attack == 0:
                a2 = self.player2.arcane_blast(self.player1)
            elif enemy_attack == 1:
                a2 = self.player2.fireball(self.player1)
            elif enemy_attack == 2:
                a2 = self.player2.electrify(self.player1)




        if self.player1.hit_points <= 0 and self.player2.hit_points > 0:
            self.player1.hit_points = 0
            self.end["text"] = str(self.player2.name) + " is victorious!"
            self.button = tkinter.Button(self, text = "Exit", command = self.exit_clicked, fg = "red", bg = "black", width = 10)
            self.button.grid(row = 9, column = 1)
        elif self.player2.hit_points <= 0 and self.player1.hit_points > 0:
            self.player2.hit_points = 0
            self.end["text"] = str(self.player1.name) + " is victorious!"
            self.button = tkinter.Button(self, text = "Exit", command = self.exit_clicked, fg = "red", bg = "black", width = 10)
            self.button.grid(row = 9, column = 1)
        elif self.player1.hit_points <= 0 and self.player2.hit_points <= 0:
            self.player1.hit_points = 0
            self.player2.hit_points = 0
            self.end["text"] = "It's a tie!"
            self.button = tkinter.Button(self, text = "Exit", command = self.exit_clicked, fg = "red", bg = "black", width = 10)
            self.button.grid(row=9, column=1)

        self.you["text"] = str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP"
        self.enemy["text"] = str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP"
        self.attack_label1= tkinter.Label(self, text = a1)
        self.attack_label1.grid(row = 5, column = 1)
        self.attack_label2 = tkinter.Label(self, text = a2)
        self.attack_label2.grid(row = 6, column = 1)



                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.call_on_selected()
  
            
            
            
            