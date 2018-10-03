#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

class Fix_Sub:
    """
    This class handles sub fixes by current player
    """
    
    def fix_sub(self, dic_ships, dic_pos, list_players):

        # Error Handling
        def fix_input_err():
            print('\n*********************************************')
            print('That choice is invalid. Please try again!')
            print('*********************************************')
            fix_input()

        # Error Handling 2
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
        
        fix_input()
