<?php

/* fourLetterWords
Write a function that takes a sentence and returns the number of four letter
words it contains. Dont worry about handling punctuation 
*/


# If punctuation doesn't matter (as problem states):
function four_letter_words($s) {
    $res = 0;
    $words = preg_split('/\s+/', $s);
    foreach($words as $w) {
        if (strlen($w) === 4) 
            $res += 1;
    }
    return $res;
}


/* Alternative: if punctuation matters and have to be accounted for:

function four_letter_words($s) {
    $res = 0;
    $words = preg_split('/\W+/', $s);
    foreach($words as $w) {
        if (strlen($w) === 4) 
            $res += 1;
    }
    return $res;
}

*/


echo four_letter_words("This sentence is fine"), "\n"; # 2
echo four_letter_words("So is this one"), "\n"; # 1
echo four_letter_words("Hello"), "\n"; # 0
echo four_letter_words("This sentence is different, it has punctuation!!!"), "\n"; # 1
#echo four_letter_words("This one is tricky !!!!"), "\n"; # 1 #this test is for variants where punctuation matters
