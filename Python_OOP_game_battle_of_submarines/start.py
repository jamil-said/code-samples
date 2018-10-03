#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

from print_manual import Print_Manual

class Start:
    """
    This class collects information from the players at the beginning of
    the game and forwards it to the game setting class
    """
    
    def start_game(self):
        
        # Create game objects 
        dic_players = {}
        print_manual_obj = Print_Manual()
        
        # Welcome greeting
        def prompt_start():
            print('\n********************************************************')
            print('Welcome to the Battle of Submarines Game!')
            print('This game can be played by 2, 3 or 4 players.')
            print('********************************************************\n')
            prompt_control()

        # Prompt with initial options
        def prompt_control():
            manual, exiting, starting = {'M', 'm'}, {'E', 'e'}, {'S', 's'}
            prompt = '* To start a new game, press "s" and press "Enter".' 
            prompt += '\n* To read the game manual, press "m" and press "Enter".'
            prompt += ' \n* To exit, press "e" and press "Enter".'
            prompt += '\n\nAhoy, Captain! Make your choice:\n'
            ans = input(prompt)
            if ans in manual: 
                print_manual_obj.print_manual()
                prompt_control()
            elif ans in exiting:
                return
            elif ans in starting:
                start_input()
            else:
                error_input_start()

        # Handle input error on initial options
        def error_input_start():
            print('\n**************************************************************')
            print('Sailor! You must enter "s" to start, "m" to read the manual')
            print('or "e" to exit! Is that so difficult? Next time you will peel')
            print('potatoes for a long time!')
            print('**************************************************************\n')
            prompt_control()

        # Collect players information. Replace certain punctuation characters
        # from player's input (ex: ',', ':', etc.) not to interfere with code later
        # Players input will also be joined with player number for security and control
        # Give each player 3 subs, one of each type (to be defined later)
        def start_input():
            set_players = {'2', '3', '4'}
            prompt = '\nAhoy, Captain! How many players will play? (2, 3 or 4)\n'
            play_num = input(prompt)
            if play_num not in set_players: 
                error_input_play()
                return
            for i in range(1, int(play_num)+1):
                prompt = '\nAye, Sir! What is the name of the player {}?'.format(i,)
                prompt += ' (Limit 10 characters)\n'
                ans = input(prompt)
                ans.replace(',',';').replace('(','[').replace(')',']').replace(':','-').replace('_','-')
                play_name = ans if len(ans) <= 10 else ans[:10]
                dic_players['Player'+str(i)+'_'+play_name] = 3

        # Handle error in players' information input
        def error_input_play():
            print('\n**************************************************************')
            print('Sailor! You must enter 2, 3 or 4. Is that so difficult?')
            print('Go clean the sub bathrooms and then try again!')
            print('**************************************************************')
            start_input()
        
        prompt_start()
        
        return dic_players
