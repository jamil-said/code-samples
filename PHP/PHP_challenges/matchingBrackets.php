<?php

/*
A string of brackets is correctly matched if you can pair every opening 
bracket up with a later closing bracket. For example, "(()())" is correctly 
matched and "(()" and ")(" are not. Implement a function which takes a string 
of brackets and returns the minimum number of brackets you'd have to add 
to the string to make it correctly matched. For example, "(()" could be 
correctly matched by adding a single closing bracket at the end, so you 
would return 1. ")(" can be correctly matched by adding an opening bracket 
at the start and a closing bracket at the end, so you'd return 2. If your
string is already correctly matched, you can just return 0.
*/


function brackets($bckt) {
    $opn = 0;
    $bct = 0;
    $arr = str_split($bckt);
    foreach($arr as $c) {
        if($c === '(')
            $opn += 1;
        elseif($c === ')') {
            if($opn > 0)
                $opn -= 1;
            else
                $bct += 1;
        }
    }
    return $opn + $bct;
}


echo brackets('(()()()())'), "\n"; #0
echo brackets('(()())'), "\n"; #0
echo brackets('((())'), "\n"; #1
echo brackets('())'), "\n"; #1
echo brackets(')('), "\n"; #2
echo brackets(')(())'), "\n"; #1
echo brackets('))((()'), "\n"; #4
echo brackets('))()'), "\n"; #2
echo brackets(')(('), "\n"; #3
echo brackets('((('), "\n"; #3
echo brackets(')))'), "\n"; #3
echo brackets('ab())'), "\n"; #1
