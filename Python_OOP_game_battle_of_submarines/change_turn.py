#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Change_Turn:
    """
    This class changes the turn to play to the next player
    """

    # Change turn to the next player
    def change_turn(self, list_players):
        popped = list_players.pop(0)
        list_players.append(popped)
        return
