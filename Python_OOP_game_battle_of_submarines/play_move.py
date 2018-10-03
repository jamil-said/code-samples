#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Play_Move:
    """
    This class shows current player's subs and handles player's sub moving
    """
    
    def play_move(self, cur_play_ships, dic_pos):

        # Error handling
        def play_move_input_err(cur_play_ships):
            print('\n*********************************************')
            print('That choice is invalid. Please try again!')
            print('*********************************************')
            play_move_input(cur_play_ships)

        # Error handling
        def play_move_input_err2(cur_play_ships, ans, err):
            print('\n*********************************************')
            print(err)
            print('*********************************************')
            play_move_input2(cur_play_ships, ans)

        # Show current player his/her subs and get input which to move
        def play_move_input(cur_play_ships):
            mes = '\nThe Captain with the turn may only control his own subs! '
            mes += 'Here is a list of subs the Captain may choose to move:\n'
            print(mes)
            for i, ele, in enumerate(cur_play_ships):
                mes_ships = '{} - {}'.format(i+1, ele)
                print(mes_ships)
            prompt = '\nPlease press the option number of sub to move. (ex: "1")\n'
            ans = input(prompt)
            if not ans.isdigit() or not 0 < int(ans) <= len(cur_play_ships):
                play_move_input_err(cur_play_ships)
                return
            play_move_input2(cur_play_ships, ans)

        # Get coordinates of the move, test them and move sub
        def play_move_input2(cur_play_ships, ans):
            move_tuple = tuple()
            new_coor = tuple()
            old_c_tuple = tuple()
            count = 0
            print('\nYou chose to move the following ship:\n')
            print(cur_play_ships[int(ans)-1])
            prompt = '\nNow please enter the move you want to execute on this ship. '
            prompt += '\nPlease note you may move UP TO a TOTAL of 30 units in any '
            prompt += '\ndirection, for ex.: 0 0 30 or 5 -15 3, and please note all  '
            prompt += '\nresulting coordinates must be within the battlefield (i.e.: '
            prompt += '\nbetween 0 0 0 and 100 100 100), and there may be no sub '
            prompt += '\nalready on the resulting coordinates. You must enter '
            prompt += '\n3 numbers, each of them separated from the next by a space.'
            prompt += '\nThe numbers can be positive or negative. Whatever numbers '
            prompt += '\nyou enter will be added to the current coordinates of the sub.'
            prompt += '\nFor example, if your coordinates are 30 30 30 and you enter '
            prompt += '\n5 -15 3, the resulting coodinates will be 35 15 33.'
            prompt += '\n\nPlease enter your move now (ex: 5 -15 3):\n'
            move = input(prompt)
            move = move.split()
            if len(move) != 3:
                err = 'You provided a wrong number of coordinates'
                play_move_input_err2(cur_play_ships, ans, err)
                return
            for i in move:
                if not i.lstrip("-").isdigit():
                    err = 'Coordinates must be numbers separated by a space'
                    play_move_input_err2(cur_play_ships, ans, err)
                    return
                else:
                    move_tuple += (int(i),)
                    count += abs(int(i))
            if count > 30:
                err = 'Absolute move sum must be equal or less than 30'
                play_move_input_err2(cur_play_ships, ans, err)
                return
            old_c = cur_play_ships[int(ans)-1]
            old_c = old_c[old_c.find("(")+1:old_c.find(")")]
            old_c = old_c.split(', ')
            for i, ele in enumerate(old_c):
                if 0 <= int(ele) + move_tuple[i] <= 100:
                    new_coor += (int(ele) + move_tuple[i],)
                    old_c_tuple += (int(ele),)
                else:
                    err = ' All resulting coordinates must be between 0 and 100'
                    play_move_input_err2(cur_play_ships, ans, err)
                    return
            if new_coor in dic_pos:
                err = 'Error! There is already a sub on the resulting coordinates'
                play_move_input_err2(cur_play_ships, ans, err)
                return
            else:
                dic_pos[new_coor] = dic_pos[old_c_tuple]
                dic_pos.pop(old_c_tuple)
            print('\nSuccess. The ship was moved to the new position:')
            print(new_coor, dic_pos[new_coor])

        play_move_input(cur_play_ships)
