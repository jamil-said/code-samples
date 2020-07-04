<?php

/* mazeSmallestPathToTreasure
Given a maze (a 2d array), and considering that you can traverse the maze 
where the value is 1 and cannot traverse it when the value is 0, find the 
smallest path from the upper left corner of the maze to the treasure, 
which is hidden somewhere in the maze (the treasure has value 5, and there's 
only one treasure in the maze). If there's no viable path to the treasure, 
return -1. There are only 1, 0, and 5 values in the maze. Return an integer 
that represents the minimum path value which has to be traversed to arrive 
at the treasure.

For example:

maze = [[1, 0, 0], 
        [1, 0, 0], 
        [1, 5, 1]]
        
would return 3, as one would have to traverse the maze elements (0,0),
(1,0),(2,0) to arrive at the treasure located at (2,1)
*/


# I think this solution is right, but it was not tested with a large test case
function mazeFind($maze) {
    if(empty($maze) || empty($maze[0]))
        return -1;
    $result = [];
    calc([], $maze, [], 0, 0, $result);
    return isset($result[0]) ? $result[0] : -1;
}

# Note here $result is passed as a reference by adding the "&" (&$result)
function calc($path, $maze, $vis, $i, $j, &$result) {
    if(isset($vis["$i,$j"]))
        return;
    elseif(($i >= count($maze) or $i < 0) || ($j >= count($maze[0]) or $j < 0) || ($maze[$i][$j] == 0))
        return;
    elseif((!empty($result)) && (count($path) >= $result[0]))
        return;
    if($maze[$i][$j] === 5) {
        if(!empty($result))
            $result[0] = min(count($path),$result[0]);
        else
            $result[] = count($path);
    }
    else {
        $visCopy = $vis;
        $visCopy["$i,$j"] = 1;
        $path[]=1;
        calc($path, $maze, $visCopy, $i+1, $j, $result);
        calc($path, $maze, $visCopy, $i, $j+1, $result);
        calc($path, $maze, $visCopy, $i-1, $j, $result);
        calc($path, $maze, $visCopy, $i, $j-1, $result);
    }
}
    

echo mazeFind([[1, 0, 0], [1, 0, 0], [1, 5, 1]]), "\n"; #3
echo mazeFind([[1, 1, 1, 1], 
                [0, 1, 1, 1], 
                [0, 1, 0, 1], 
                [1, 1, 5, 1], 
                [0, 0, 1, 1]]), "\n"; #5
echo mazeFind([[0, 0, 0], [1, 0, 0], [1, 5, 1]]), "\n"; #-1
echo mazeFind([[5, 0, 0], [1, 0, 0], [1, 0, 1]]), "\n"; # 0
echo mazeFind([[]]), "\n"; # -1
echo mazeFind([]), "\n"; # -1
echo mazeFind([[1,1,1,1,1,1],
                [1,0,0,0,1,1],
                [1,0,5,0,1,1],
                [1,1,1,0,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1]]), "\n"; #6
echo mazeFind([[1,1,1,1,1,1],
                [1,0,0,0,1,1],
                [1,0,5,0,1,1],
                [1,0,1,0,1,1],
                [1,1,1,0,1,1],
                [1,1,1,1,1,1]]), "\n"; #8
