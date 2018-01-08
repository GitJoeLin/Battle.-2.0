import tkinter

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
        self.button = tkinter.Button(self, text = "Attack", command = self.attack_clicked, fg = "red", bg = "black") \
            .grid(row = 0, column = 0)
        self.atk1 = tkinter.Label(self, text = "")
        self.atk1.grid(row = 1, column = 1)
        self.atk2 = tkinter.Label(self, text = "")
        self.atk2.grid(row = 2, column = 1)
        self.end = tkinter.Label(self, text = "")
        self.end.grid(row = 3, column = 1)
        tkinter.Label(self, text = "You").grid(row = 5, column = 0)
        tkinter.Label(self, text = "Computer").grid(row = 5, column = 1)
        imageLarge = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label(self, image=imageLarge, )
        w.photo = imageLarge
        w.grid(row = 4, column=0, sticky=tkinter.W)
        imageLarge2 = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        x = tkinter.Label(self, image=imageLarge2, )
        x.photo = imageLarge2
        x.grid(row = 4, column=1, sticky=tkinter.W)
        self.you = tkinter.Label(self, text = str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP")
        self.you.grid(row = 6, column = 0)
        self.enemy = tkinter.Label(self, text = str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP")
        self.enemy.grid(row = 6, column = 1)
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and the computer.
            2) Updates the labels on the top right with the result of the attacks.
            3) Determines if there is a victor.
            4) If there is a victor, removes that Attack button and replaces it with an Exit button.     
        '''        
        a1 = self.player1.attack(self.player2)
        a2 = self.player2.attack(self.player1)

        if self.player1.hit_points <= 0 and self.player2.hit_points > 0:
            self.player1.hit_points = 0
            self.end["text"] = str(self.player2.name) + " is victorious!"
            self.button = tkinter.Button(self, text = "Exit", command = self.exit_clicked, fg = "red", bg = "black", width = 10) \
            .grid(row = 0, column = 0)
        elif self.player2.hit_points <= 0 and self.player1.hit_points > 0:
            self.player2.hit_points = 0
            self.end["text"] = str(self.player1.name) + " is victorious!"
            self.button = tkinter.Button(self, text = "Exit", command = self.exit_clicked, fg = "red", bg = "black", width = 10) \
            .grid(row = 0, column = 0)
        elif self.player1.hit_points <= 0 and self.player2.hit_points <= 0:
            self.player1.hit_points = 0
            self.player2.hit_points = 0
            self.end["text"] = "It's a tie!"
            self.button = tkinter.Button(self, text = "Exit", command = self.exit_clicked, fg = "red", bg = "black", width = 10) \
            .grid(row = 0, column = 0)

        self.you["text"] = str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP"
        self.enemy["text"] = str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP"
        self.atk1["text"] = a1
        self.atk2["text"] = a2



                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.call_on_selected()
  
            
            
            
            