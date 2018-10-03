#!/usr/bin/env python3

# Battle of Submarines 
# Code by Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
# Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment

from game_over import Game_Over

class Attack_Sub:
    """
    This class handles sub attacks by current player
    """
    
    def attack_sub(self, dic_players, dic_ships, dic_pos, list_players):
        
        # Creating game end handling object
        game_over_obj = Game_Over()
        
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
                    game_over_obj.game_over(player_n, dic_players, list_players)                    
            else:
                mes = '\nSuccess! the sub {} was attacked and the damage '.format(sub_name,)
                mes += 'level now is {}.'.format(dic_ships[sub_name].damage_level,)
                print(mes)
            return
        
        attack_input()
        
        return len(list_players)
