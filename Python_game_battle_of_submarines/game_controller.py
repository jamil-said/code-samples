#!/usr/bin/env python3

# Battle of Submarines
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Game_Controller:
    """
    This class receives game objects from another class, starts the game 
    and controls its flow until the end.
    """
    
    def game_controller(self, dic_players, dic_ships, dic_pos, list_players):
        
        #show players the play order
        def show_player_order():
            print('\n**************************************************************')
            print('Captains, here is the playing order (randomly selected):\n')
            for i, p in enumerate(list_players):
                mes = '{} - {}'.format(i+1,p)
                print(mes)
            print('**************************************************************')
            play_turn()
       
        # Show all subs in the battlefield and find current player ships
        def play_turn():
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
            play_move_input(cur_play_ships)
        
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
            attack_input()
        
        # Error handling
        def attack_input_err():
            print('\n*********************************************')
            print('That choice is invalid. Please try again!')
            print('*********************************************')
            attack_input()

        # Error handling
        def attack_input_err2(cur_play_ships, ans_att):
            print('\n*********************************************')
            print('That choice is invalid. Please try again!')
            print('*********************************************')
            attack_input2(cur_play_ships, ans_att)
        
        # Show subs and ask which sub to attack with    
        def attack_input():
            cur_play_ships = []
            mes = '\nHere are all the subs in the game (updated), with coordinates '
            mes += '& damage level (0-5, being that 5 destroys sub!):\n'
            print(mes)
            for i in sorted(((v,k) for k,v in dic_pos.items())):
                mes = 'Sub: {}, Coordinates: {}, Damage Level {}'.format(i[0]
                , i[1], dic_ships[i[0]].damage_level)
                if mes.startswith(list_players[0], 5):
                    cur_play_ships.append(mes)
                print(mes)
            for i in cur_play_ships:
                if i.split(',')[0].endswith('Fixer'):
                    cur_play_ships.remove(i)
            if not cur_play_ships:
                mes_ship = '\nYou have no attacking ships left. Your attacking '
                mes_ship += 'turn was forfeited\n'
                print(mes_ship)
                fix_input()
                return
            mes = '\nHere is a list of the subs the Captain may choose '
            mes += 'to attack with:\n'
            print(mes)
            for i, ele, in enumerate(cur_play_ships):
                mes_ships = '{} - {}'.format(i+1, ele)
                print(mes_ships)
            prompt = '\nPlease enter the number of the sub to attack with. Ex: "1"\n'
            ans_att = input(prompt)
            if not ans_att.isdigit() or not 0 < int(ans_att) <= len(cur_play_ships):
                attack_input_err()
                return
            print('\nYou chose to attack with the following ship:')
            print(cur_play_ships[int(ans_att)-1])
            attack_input2(cur_play_ships, ans_att)

        # Check attackable subs and ask which one to attack
        def attack_input2(cur_play_ships, ans_att):
            attack_c = tuple()
            targets = []
            tmp_c = cur_play_ships[int(ans_att)-1]
            tmp_c = tmp_c[tmp_c.find("(")+1:tmp_c.find(")")]
            tmp_c = tmp_c.split(', ')
            for i, ele in enumerate(tmp_c):
                attack_c += (int(ele),)
            for key in dic_pos.keys():
                if key == attack_c or dic_pos[key].startswith(list_players[0]):
                    continue
                dia = ((attack_c[0]-key[0])**2 + (attack_c[1]-key[1])**2 + (
                attack_c[2]-key[2])**2)**0.5
                if dia <= 20:
                    m = 'Sub: {}, Coordinates: {}, Distance: {}, Damage Level: {}'.format(
                    dic_pos[key], key, dia, dic_ships[dic_pos[key]].damage_level)
                    targets.append(m)
            if not targets:
                mes_ship = '\nThere is no enemy sub within 20 units distance '
                mes_ship += 'for an attack. Your attack turn was forfeited.'
                print(mes_ship)
                fix_input()
                return
            mes = '\nThe following subs are within range (20 units distance) '
            mes += 'for an attack. Please note that an attack to a sub '
            mes += 'within 10 units distance inflicts twice the damage!\n'
            print(mes)
            for i, ele in enumerate(targets):
                mes_a = '{} - {}'.format(i+1, ele)
                print(mes_a)
            prompt = '\nPlease enter the number of the sub to attack. Ex: "1"\n'
            ans_tgt = input(prompt)
            if not ans_tgt.isdigit() or not 0 < int(ans_tgt) <= len(targets):
                attack_input_err2(cur_play_ships, ans_att)
                return
            sub_attacked = targets[int(ans_tgt)-1]
            attack_handler(sub_attacked)

        # Attack the sub and handle consequences
        def attack_handler(sub_attacked):
            coo_tuple = tuple()
            sub_name = sub_attacked[sub_attacked.find("Sub: ")+5:sub_attacked.find(",")]
            player_n = sub_name[:sub_name.find("_Sub")]
            dist = float(sub_attacked.split("Distance: ")[1][:sub_attacked.split(
            "Distance: ")[1].find(",")])
            dmg = 1 if dist > 10 else 2
            dic_ships[sub_name].damage_level += dmg
            tmp_c = sub_attacked[sub_attacked.find("(")+1:sub_attacked.find(")")]
            tmp_c = tmp_c.split(', ')
            for i in tmp_c:
                coo_tuple += (int(i),)
            if dic_ships[sub_name].damage_level >= 5:
                mes = '\nSuccess! the sub {} was destroyed and is no more!'.format(sub_name,)
                print(mes)
                dic_ships.pop(sub_name)
                dic_pos.pop(coo_tuple)
                dic_players[player_n] -= 1
                if dic_players[player_n] <= 0:
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
                        return
            else:
                mes = '\nSuccess! the sub {} was attacked and the damage '.format(sub_name,)
                mes += 'level now is {}.'.format(dic_ships[sub_name].damage_level,)
                print(mes)
            fix_input()
            return

        # Error Handling
        def fix_input_err():
            print('\n*********************************************')
            print('That choice is invalid. Please try again!')
            print('*********************************************')
            fix_input()

        # Error Handling
        def fix_input_err2(cur_play_ships, ans_fix):
            print('\n*********************************************')
            print('That choice is invalid. Please try again!')
            print('*********************************************')
            fix_input2(cur_play_ships, ans_fix)

        # Show subs and ask which sub to fix with
        def fix_input():
            cur_play_ships = []
            mes = '\nHere are all the subs in the game (updated), with coordinates '
            mes += '& damage level (0-5, being that 5 destroys sub!):\n'
            print(mes)
            for i in sorted(((v,k) for k,v in dic_pos.items())):
                mes = 'Sub: {}, Coordinates: {}, Damage Level {}'.format(i[0]
                , i[1], dic_ships[i[0]].damage_level)
                if mes.startswith(list_players[0], 5):
                    cur_play_ships.append(mes)
                print(mes)
            for i in cur_play_ships:
                if i.split(',')[0].endswith('Attacker'):
                    cur_play_ships.remove(i)
            if not cur_play_ships:
                mes_ship = '\nYou have no fixing ships left. Your fixing '
                mes_ship += 'turn was forfeited\n'
                print(mes_ship)
                change_turn()
                return
            mes = '\nHere is a list of the subs the Captain may choose '
            mes += 'to fix with:\n'
            print(mes)
            for i, ele, in enumerate(cur_play_ships):
                mes_ships = '{} - {}'.format(i+1, ele)
                print(mes_ships)
            prompt = '\nPlease enter the number of the sub to fix with. Ex: "1"\n'
            ans_fix = input(prompt)
            if not ans_fix.isdigit() or not 0 < int(ans_fix) <= len(cur_play_ships):
                fix_input_err()
                return
            print('\nYou chose to fix with the following ship:')
            print(cur_play_ships[int(ans_fix)-1])
            fix_input2(cur_play_ships, ans_fix)

        # Show fixable subs and ask which sub to be fixed
        def fix_input2(cur_play_ships, ans_fix):
            fix_c = tuple()
            targets = []
            tmp_c = cur_play_ships[int(ans_fix)-1]
            tmp_c = tmp_c[tmp_c.find("(")+1:tmp_c.find(")")]
            tmp_c = tmp_c.split(', ')
            for i in tmp_c:
                fix_c += (int(i),)
            for key in dic_pos.keys():
                if key == fix_c or dic_pos[key].startswith(list_players[0]) == False:
                    continue
                dia = ((fix_c[0]-key[0])**2 + (fix_c[1]-key[1])**2 + (
                fix_c[2]-key[2])**2)**0.5
                if dia <= 20:
                    m = 'Sub: {}, Coordinates: {}, Distance: {}, Damage Level: {}'.format(
                    dic_pos[key], key, dia, dic_ships[dic_pos[key]].damage_level)
                    targets.append(m)
            if not targets:
                mes_ship = '\nThere is no friendly sub within 20 units distance '
                mes_ship += 'for a fix. Your fix turn has been forfeited.'
                print(mes_ship)
                change_turn()
                return
            mes = '\nThe following subs are within range (20 units distance) '
            mes += 'for a fix. Please note that fixing a sub within '
            mes += '10 units distance fixes twice the damage!\n'
            print(mes)
            for i, ele in enumerate(targets):
                mes_a = '{} - {}'.format(i+1, ele)
                print(mes_a)
            prompt = '\nPlease enter the number of the sub to fix. Ex: "1"\n'
            ans_tgt = input(prompt)
            if not ans_tgt.isdigit() or not 0 < int(ans_tgt) <= len(targets):
                fix_input_err2(cur_play_ships, ans_fix)
                return
            sub_fixed = targets[int(ans_tgt)-1]
            fix_handler(sub_fixed)

        # Fix the sub and handle consequences
        def fix_handler(sub_fixed):
            sub_name = sub_fixed[sub_fixed.find("Sub: ")+5:sub_fixed.find(",")]
            dist = float(sub_fixed.split("Distance: ")[1][:sub_fixed.split(
            "Distance: ")[1].find(",")])
            fix = 1 if dist > 10 else 2
            dic_ships[sub_name].damage_level -= fix
            if dic_ships[sub_name].damage_level < 0:
                dic_ships[sub_name].damage_level = 0
            mes = '\nSuccess! the sub {} was fixed and the damage '.format(sub_name,)
            mes += 'level now is {}.'.format(dic_ships[sub_name].damage_level,)
            print(mes)
            change_turn()
        
        # Change turn to the next player
        def change_turn():
            popped = list_players.pop(0)
            list_players.append(popped)
            play_turn()
            return

        show_player_order()
