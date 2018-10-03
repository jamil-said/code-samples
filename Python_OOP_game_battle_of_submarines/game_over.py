#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Game_Over:
    """
    This class checks for game ending for a player or all players
    """

    # check for game ending for a player or all players
    def game_over(self, player_n, dic_players, list_players):
        mes = '\nCaptain {} sunk along with the last sub!'.format(player_n,)
        mes += '\nGame over for Captain {}! Bye Bye! Bon Voyage!'.format(player_n,)
        print(mes)
        dic_players.pop(player_n)
        list_players.remove(player_n)
        if len(list_players) == 1:
            mes = '\nCaptain {} is the Winner of this game!'.format(list_players[0],)
            mes += '\nCongratulations Captain {}! Well done!'.format(list_players[0],)
            mes += '\nGame Over! Thanks for playing!\n'
            print(mes)
