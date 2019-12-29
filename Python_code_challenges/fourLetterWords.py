""" fourLetterWords
Write a function that takes a sentence and returns the number of four letter
words it contains. Dont worry about handling punctuation 
"""

# If punctuation doesn't matter (as problem states):
def four_letter_words(s):
    count = 0
    arr = s.split()
    for w in arr:
        if len(w) == 4:
            count += 1
    return count


# Alternative: if punctuation matters and have to be accounted for:
import re
def four_letter_words(s):
    count = 0
    arr = re.split(r'\W+', s)
    for w in arr:
        if len(w) == 4:
            count += 1
    return count
    
    
#alternative, if punctuation matters (slower but more specific):
def four_letter_words(s):
    res, temp = 0, 0
    for w in s.split():
        for c in w:
            if c.isalpha(): 
                temp += 1
        if temp == 4: 
            res += 1
        temp = 0
    return res


print(four_letter_words("This sentence is fine")) # 2
print(four_letter_words("So is this one")) # 1
print(four_letter_words("Hello")) # 0
print(four_letter_words("This sentence is different, it has punctuation!!!")) # 1
print(four_letter_words("This one is tricky !!!!")) # 1 #this test is for variants where punctuation matters
