# Battle of Submarines -- Python 3 Battleship Game Played in a 3D Battlefield

## How to Run the Game

This game is text-based and a little rudimentary, but it runs smoothly (as far as I know!). One way to run this game is the following:

* Copy game folder to your computer and make sure to make all .py files executable
* Open Bash (shell) terminal
* Change the working directory to the game directory (e.g.: cd /battleofsubs)
* Type ./game.py and then press "Enter"
    
After the game starts, you will be given the chance to read the game's rules (manual) on the terminal at the very beginning of the game. The game manual is read from a text file located on the game's folder (manual.txt). The game's rules are also shown below.

## Game Rules (Manual)

* 2 to 4 players can play the game.

* Submarines (subs, for short!) will be assigned randomly to players at the beginning.

* Each player will get one sub of each class. There are 3 types of subs: 
    * Subs class "A" are attackers, and can attack other subs. 
    * Subs class "F" are fixers, and can fix other damaged subs. 
    * Subs class "M" are masters, and can fix or attack other subs. 

* The game will start with a player picked randomly, and then it will follow the player number order (ex: if player 3 plays first, then next is player 4, then player 1, etc.).

* The battlefield is a 3D ocean "cube" with corners (0,0,0) and (100,100,100)

* On a turn, a player can do all 3 of those actions (one of each, in order): 
    * Move a sub: from 0 to 30 units in any direction (up, down, left, right, back or forward) to a spot not currently occupied by any other sub (ex: 0,0,0 to 0,0,30 or 0,0,0 to 5,10,15).
    * Attack a sub: attack an enemy sub situated within 20 units distance (including the "diagonal" distance).
    * Fix a sub: fix a friendly sub situated within 20 units distance (including the "diagonal" distance). 

* An attack on a sub will cause damage. If the sub is within 10 units of distance or less at the time of the attack, the attack will increase the sub damage by 2 levels. If the sub is between 11 to 20 units of distance at the time of the attack, the attack will increase the sub damage by 1 level.

* Any sub will be destroyed if they sustain damage level 5 or higher; and if a sub is destroyed, it is out of the game for good! 

* You may only attack enemy subs.

* A fix applied to a sub will fix damage. If the sub is within 10 units of distance or less at the time of the fix, the fix will decrease the sub damage by 2 levels (up to zero level of damage). If the sub is between 11 to 20 units of distance at the time of the fix, the fix will decrease the sub damage by 1 level (up to zero level of damage). If you fix a sub which already has level of damage 0, it will remain unchanged.

* You may only fix friendly (your own) subs. Note: a sub cannot fix itself.

* A player exits the game when all of his/hers subs have been destroyed.

* The last player that remains with subs in the battlefield is the winner!

### Python Code Author
Jamil Said Jr -- Copyright (C) 2018 Jamil Said Jr

### Game Development Environment
Developed on a Debian 9, Python 3.5.3, GNU Bash 4.4.12 environment
