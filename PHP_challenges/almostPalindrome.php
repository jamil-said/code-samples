<?php

/*
The Palindromic score of a string is the number of errors (characters which
do not match) when the string is read forwards and backwards. For example, 
the palindromic score of 'fox' is 2, because 'fox' and 'xof' differ by two
characters. Write a function to take a string and return its palindromic 
score. 
*/

class Solution {
    function apalin($word) {
        $palindex = 0;
        $lenStr = strlen($word);
        foreach (range(0, $lenStr-1) as $i) {
            if ($word[$i] !== $word[($lenStr-1)-$i])
                $palindex += 1;
        }
        return $palindex;
    }
}


echo Solution::apalin('abba'), "\n"; #0
echo Solution::apalin('abcdcaa'), "\n"; #2
echo Solution::apalin('fox'), "\n"; #2
echo Solution::apalin('aaabbb'), "\n"; #6

