<?php

/* diagonalTraverseFromTop
Given an MxN matrix, write code which prints out the diagonals (from upper left
to lower right) of the matrix. In this example where M = 3, N = 4:

[[9 3 2]
 [8 6 1]
 [5 5 6]
 [1 2 8]]

Your code should print out:
9
3 8
2 6 5
1 5 1
6 2
8
*/

function printMtx($arr) {
    foreach(range(0, count($arr[0])-1) as $idX){
        printDia($arr, $idX, 0, '');
    }
    foreach(range(1, count($arr)-1) as $idY) {
        printDia($arr, count($arr[0])-1, $idY, '');
    }
}

function printDia($arr, $idX, $idY, $res) {
    while($idY < count($arr) and $idX >= 0) {
        $res = $res . strval($arr[$idY][$idX]) . ' ';
        $idY += 1;
        $idX -= 1;
    }
    echo substr($res, 0, -1), "\n";
}


printMtx([[9,3,2], [8,6,1], [5,5,6], [1,2,8]]);
/*
9
3 8
2 6 5
1 5 1
6 2
8
*/
