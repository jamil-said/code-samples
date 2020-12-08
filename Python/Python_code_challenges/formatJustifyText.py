""" formatJustifyText
Given an array of words and a length l, format the text such that each 
line has exactly l characters and is fully justified on both the left and 
the right. Words should be packed in a greedy approach; that is, pack as 
many words as possible in each line. Add extra spaces when necessary so 
that each line has exactly l characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots 
on the right. For the last line of text and lines with one word only, 
the words should be left justified with no extra space inserted between 
them.

Example

For
words = ["This", "is", "an", "example", "of", "text", "justification."]
and l = 16, the output should be

textJustification(words, l) = ["This    is    an",
                               "example  of text",
                               "justification.  "]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string words

An array of words. Each word is guaranteed not to exceed l in length.

Guaranteed constraints:
1 ≤ words.length ≤ 150,
0 ≤ words[i].length ≤ l.

[input] integer l

The length that all the lines in the output array should be.

Guaranteed constraints:
1 ≤ l ≤ 60.

[output] array.string

The formatted text as an array containing lines of text, with each line having a length of l.
"""

def textJustification(words, l):
    result, begin, lnght = [], 0, 0
    for i in range(len(words)):
        if lnght + len(words[i]) + (i - begin) > l:
            result += joining(words, l, begin, i, lnght, False),
            begin, lnght = i, 0
        lnght += len(words[i])
    result += joining(words, l, begin, len(words), lnght, True),
    return result

def spaceAdd(i, cntSpace, l, lastLine):
    if i < cntSpace:
        return 1 if lastLine else (l // cntSpace) + int(i < l % cntSpace)
    return 0

def joining(words, l, begin, end, lnght, lastLine):
    s, n = [], end - begin
    for i in range(n):
        s += words[begin + i],
        s += ' ' * spaceAdd(i, n - 1, l - lnght, lastLine),
    line = "".join(s)
    if len(line) < l:
        line += ' ' * (l - len(line))
    return line

print(textJustification(["This", "is", "an", "example", "of", "text", "justification."],
16))
"""
["This    is    an",
 "example  of text",
 "justification.  "]
"""

