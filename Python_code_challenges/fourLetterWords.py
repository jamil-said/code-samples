
""" fourLetterWords -- 4 minutes
Write a function that takes a sentence and returns the number of four letter
words it contains. Dont worry about handling punctuation 
"""

def four_letter_words(sentence):
    result = 0
    for i in sentence.split():
        if len(i) == 4: result += 1
    return result

""" #alternative, checks if all chars are alpha in len 4 strings
def four_letter_words(sentence):
    result, temp = 0, 0
    for i in sentence.split():
        for j in i:
            if j.isalpha(): temp += 1
        if temp == 4: result += 1
        temp = 0
    return result
"""

print(four_letter_words("This sentence is fine")) # 2
print(four_letter_words("So is this one")) # 1
print(four_letter_words("Hello")) # 0
print(four_letter_words("This sentence is differemt, it has punctuation!!!")) # 1
#print(four_letter_words("This one is tricky !!!!")) # 1 this one only if count non alpha,



