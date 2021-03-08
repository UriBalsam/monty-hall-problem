''' Pseudo code for Monty Hall game:
    1. Launch game window, provide instructions, and show three closed doors.
    2. The user chooses a door.
    3. Reveal a non winning door from the remaining two doors.
    4. Player has the chance to switch doors
    5. If player switches, reveal new door. Otherwise reveal original door.
    6. Record results and show the statistics for each game strategy.
'''

import random
import tkinter as tk
from test.test_importlib.namespace_pkgs.project1 import parent

class Game(tk.Frame):
    """GUI application for Monty Hall game"""
    doors = ('a', 'b', 'c')
    def __init__(self, parent):
        "initialize the frame"
        super(Game, self).__init__(parent) #parent is the root window
        self.parent = parent
        self.img_file = 'all_closed.png'
        self.choice = '' #Player's door choice
        self.winner = '' #Open up the goat door
        self.first_choice_wins = 0 # the counter
        self.switch_doors_wins = 0 # Also a counter
        self.create_widgets()
    
    def create_widgets(self):
        '''Create label, button, and text widgets.'''
        # Create label to hold image of doors
        img = tk.PhotoImage(file='all_closed.png')
        self.photo_ibl = tk.Label(self.parent, image=img, 
                    text ='', borderwidth=0)
        self.photo_ibl.image = img

        #instructions label
        instr_input = [
            ('Behind one door is CASH!', 1, 0, 5, 'W'),
            ('Behind the others: A GOAT!!!', 2, 0, 5, 'W'),
            ('Pick a door:', 1, 3, 1, 'E')
        ]

        for text, row, column, columnspan, sticky in instr_input:
            instr_ibl = tk.Label(self.parent, text=text)
            instr_ibl.grid(row=row, column=column, columnspan=columnspan, sticky=sticky, ipadx=30)
            