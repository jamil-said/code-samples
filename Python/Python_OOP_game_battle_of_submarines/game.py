#!/usr/bin/env python3

# Battle of Submarines
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

import random
from start import Start
from ship_a import Ship_A
from ship_f import Ship_F
from ship_m import Ship_M
from game_controller import Game_Controller

class Game: 
    """
    This class gets players' input from another class, sets a new game 
    and fowards the new game objects to a controller class.
    """
    
    def set_game(self):
        
        # Create game objects
        dic_ships = {}
        dic_pos = {}
        list_ships_name = []
        list_players = []
        controller_obj = Game_Controller()
        start_obj = Start()
        dic_players = start_obj.start_game()
        
        # Check that players' input was received
        if not dic_players:
            return 'Game Over! We cannot play a game without players!'
       
        # Create ships names
        for key in sorted(dic_players.keys()):
            list_ships_name.append(key+'_'+'Sub_Attacker')
            list_ships_name.append(key+'_'+'Sub_Fixer')
            list_ships_name.append(key+'_'+'Sub_Master')
        
        # Instantiate ship objects and assign them to corresponding names in dictionary
        for i in range(0, len(dic_players)*3, 3):
            dic_ships[list_ships_name[i]] = Ship_A(list_ships_name[i])
            dic_ships[list_ships_name[i+1]] = Ship_F(list_ships_name[i+1])
            dic_ships[list_ships_name[i+2]] = Ship_M(list_ships_name[i+2])

        # Distribute existing ships in initial random positions (dictionary 
        # of positions)
        while list_ships_name:
            cur_pos = (random.randrange(0,100), random.randrange(0,100)
            , random.randrange(0,100))
            if cur_pos in dic_pos:
                continue
            dic_pos[cur_pos] = list_ships_name.pop()
        
        # Randomly pick first player to play and put players in ordered list
        for key in sorted(dic_players.keys()):
            list_players.append(key)
        cur_player = random.randrange(0, len(list_players))
        list_players = list_players[cur_player:] + list_players[:cur_player]

        # Send relevant game objects to the class that will start the game
        # and control its flow
        controller_obj.game_controller(dic_players, dic_ships, dic_pos
        , list_players)

if __name__ == '__main__': 
    game_obj = Game()
    game_obj.set_game()
