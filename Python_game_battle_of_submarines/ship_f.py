#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Ship_F:
    """
    This class defines Fixer Submarines (subs type "F").
    """
    
    def __init__(self, name):
        self.name = name
        self.damage_level = 0
        self.sub_type = 'F'
        self.attack = 0
        self.fix = 1

