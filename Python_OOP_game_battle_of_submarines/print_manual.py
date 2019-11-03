#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Print_Manual:
    """
    This class prints the game manual (rules) on the screen
    """

    # Print the game manual (rules) on the screen
    def print_manual(self):
        with open('manual.txt') as f_obj:
            cont_man = f_obj.read()
        print('\n' + cont_man)
