
""" longestSentenceParagraph
Task: Get the length of the longest sentence in a given paragraph. 
Sentences are marked by periods(.), commas(,) and exclamation points(!).
ex: "This  is..Some other phrase. . x D. This is the longest sentence 
at eight words." 
"""

def longestSentence(strg):
    result, temp, setC = 0, 0, {'!'}
    strg2 = strg.replace(',', ' ! ').replace('.', ' ! ').replace('!', ' ! ')
    for w in strg2.split():
        if w in setC:
            temp = 0
            continue
        temp += 1
        result = max(result, temp)
    return result


print(longestSentence("This  is..Some other phrase. . x D. This is the \
longest sentence at eight words.")) # 8


