<?php

/* makeArrayConsecutive2

Ratiorg got statues of different sizes as a present from CodeMaster for 
his birthday, each statue having an non-negative integer size. Since he 
likes to make things perfect, he wants to arrange them from smallest to 
largest so that each statue will be bigger than the previous one exactly 
by 1. He may need some additional statues to be able to accomplish that. 
Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

Input/Output

[execution time limit] 4 seconds (php)

[input] array.integer statues

An array of distinct non-negative integers.

Guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20.

[output] integer

The minimal number of statues that need to be added to existing statues 
such that it contains every integer size from an interval [L, R] (for 
some L, R) and no other sizes.

*/

function makeArrayConsecutive2($statues) {
    if(count($statues) <= 1) {
        return 0;
    }
    $nStat = 0;
    sort($statues);
    foreach (range(1, count($statues)-1) as $n) {
        $nStat += abs($statues[$n] - $statues[$n-1])-1;
    }
    return $nStat;
}

echo makeArrayConsecutive2([6, 2, 3, 8]), "\n"; # 3
echo makeArrayConsecutive2([6]), "\n"; # 0

