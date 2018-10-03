#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Show_Play_Order:
    """
    This class show players the player order at the beginning of the game.
    """
    
    #show players the play order
    def show_player_order(self, list_players):
        print('\n**************************************************************')
        print('Captains, here is the playing order (randomly selected):\n')
        for i, p in enumerate(list_players):
            mes = '{} - {}'.format(i+1,p)
            print(mes)
        print('**************************************************************')
