#!/usr/bin/env python3

# Battle of Submarines
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

from show_play_order import Show_Play_Order
from play_turn import Play_Turn
from play_move import Play_Move
from attack_sub import Attack_Sub
from fix_sub import Fix_Sub
from change_turn import Change_Turn

class Game_Controller:
    """
    This class receives game objects from other classes, starts the game 
    and controls its flow until the end.
    """
    
    def game_controller(self, dic_players, dic_ships, dic_pos, list_players):
        
        # create game controller objects
        show_play_o_obj = Show_Play_Order()
        play_turn_obj = Play_Turn()
        play_move_obj = Play_Move()
        attack_sub_obj = Attack_Sub()
        fix_sub_obj = Fix_Sub()
        change_turn_obj = Change_Turn()

        # show players the play order
        show_play_o_obj.show_player_order(list_players)

        # This loop keeps the game going until someone wins
        while True:
            
            # Show all subs in the battlefield, find current player ships
            cur_play_ships = play_turn_obj.play_turn(list_players, dic_pos, dic_ships)
            
            # Handle sub moving by current player
            play_move_obj.play_move(cur_play_ships, dic_pos)
            
            # Handle sub attacks by current player -- Note: if attack function 
            # returns 1, the game is over
            if attack_sub_obj.attack_sub(dic_players, dic_ships, dic_pos, list_players) == 1:
                return

            # Handle sub fixing by current player
            fix_sub_obj.fix_sub(dic_ships, dic_pos, list_players)

            # Change turn to the next player        
            change_turn_obj.change_turn(list_players)
