#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Play_Turn:
    """
    This class shows all subs in the battlefield, finds & returns current 
    player ships
    """

    # Show all subs in the battlefield, find & return current player ships
    def play_turn(self, list_players, dic_pos, dic_ships):
        cur_play_ships = []
        mes = '\nThis is Captain {} turn to play:\n'.format(list_players[0],)
        print(mes)
        mes = 'Here are all the subs in the game, with coordinates & '
        mes += 'damage level (0-5, being that 5 destroys sub!):\n'
        print(mes)
        for i in sorted(((v,k) for k,v in dic_pos.items())):
            mes = 'Sub: {}, Coordinates: {}, Damage Level {}'.format(i[0]
            , i[1], dic_ships[i[0]].damage_level)
            if mes.startswith(list_players[0], 5):
                cur_play_ships.append(mes)
            print(mes)
        return cur_play_ships
