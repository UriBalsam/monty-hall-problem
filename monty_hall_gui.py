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
        '''initialize the frame'''
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

        # Instructions label
        instr_input = [
            ('Behind one door is CASH!', 1, 0, 5, 'W'),
            ('Behind the others: A GOAT!!!', 2, 0, 5, 'W'),
            ('Pick a door:', 1, 3, 1, 'E')
        ]

        for text, row, column, columnspan, sticky in instr_input:
            instr_ibl = tk.Label(self.parent, text=text)
            instr_ibl.grid(row=row, column=column, columnspan=columnspan, sticky=sticky, ipadx=30)

        # Create Radio Buttons and Text Widgets
        self.door_choice = tk.StringVar()
        self.door_choice.set(None)

        a = tk.Radiobutton(self.parent, text = 'A', variable=self.door_choice,
                value='a', command=self.win_reveal)
        b = tk.Radiobutton(self.parent, text = 'B', variable=self.door_choice,
                value='b', command=self.win_reveal) 
        c = tk.Radiobutton(self.parent, text = 'C', variable=self.door_choice,
                value='c', command=self.win_reveal)               

        # Widget for switching door choice
        self.change_door = tk.StringVar()
        self.change_door.set(None)
        
        instr_ibl = tk.Label(self.parent, text = 'Switch door choice?')
        instr_ibl.grid(row=2, column=3, columnspan=1, sticky='E')

        self.yes = tk.Radiobutton(self.parent, state= 'disabled', text = 'Y',
                        variable=self.change_door, value = 'y',
                        command=self.show_final) 
        self.no = tk.Radiobutton(self.parent, state= 'disabled', text = 'N',
                        variable=self.change_door, value = 'n',
                        command=self.show_final) 

        # Widget for win statistics
        defaultbg = self.parent.cget('bg')
        self.unchanged_wins_txt = tk.Text(self.parent, width=20, 
                        height=1, wrap=tk.WORD, 
                        bg=defaultbg, fg='black',
                        borderwidth=0)
        self.changed_wins_txt = tk.Text(self.parent, width=20,
                        height=1, wrap=tk.WORD, bg=defaultbg,
                        fg='black', borderwidth=0)
        # Place widgets in the frame
        a.grid(row=1, column=4, sticky='W', padx=20)
        b.grid(row=1, column=4, sticky='N', padx=20)
        c.grid(row=1, column=4, sticky='E', padx=20)
        self.yes.grid(row=2, column=4, sticky='W', padx=20)
        self.no.grid(row=2, column=4, sticky='N', padx=20)
        self.unchanged_wins_txt.grid(row=1, column=5, columnspan=5)
        self.changed_wins_txt.grid(row=2, column=5, columnspan=5)

        