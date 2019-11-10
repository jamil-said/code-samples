<?php

/* addBinary
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
*/

class Solution {
    /**
    * @param String $a
    * @param String $b
    * @return String
    */
    function addBinary($a, $b) {
        $carry = 0;
        $result = array_fill(0, (strlen($a)>=strlen($b) ? strlen($a)+1 : strlen($b)+1), '0');
        foreach (range(1, count($result)+1) as $i) {
            $tempA = intval(substr($a, -$i, 1)) ? strlen($a)-$i >= 0 : 0;
            $tempB = intval(substr($b, -$i, 1)) ? strlen($b)-$i >= 0 : 0;
            $temp = $tempA + $tempB + $carry;
            if ($temp === 3) {
                $result[count($result)-$i] = '1'; 
                $carry = 1;
            }
            elseif ($temp === 2)
                $carry = 1;
            elseif ($temp === 1) {
                $result[count($result)-$i] = '1';
                $carry = 0;
            }
            else
                $carry = 0;
        }
        return $result[0] != '0' ? implode($result) : implode(array_slice($result, 1));
    }
}


echo Solution::addBinary("11", "1"), "\n"; #100
echo Solution::addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
"110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"), "\n"; 
#"110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"



/* Alternative. This is simple/fast but FAILS for very large numbers
class Solution {
    function addBinary($a, $b) {
        return strval(decbin(bindec($a) + bindec($b)));      
    }
}
*/
