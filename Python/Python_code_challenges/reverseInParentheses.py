""" reverseInParentheses
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

    For inputString = "(bar)", the output should be
    reverseInParentheses(inputString) = "rab";
    For inputString = "foo(bar)baz", the output should be
    reverseInParentheses(inputString) = "foorabbaz";
    For inputString = "foo(bar)baz(blim)", the output should be
    reverseInParentheses(inputString) = "foorabbazmilb";
    For inputString = "foo(bar(baz))blim", the output should be
    reverseInParentheses(inputString) = "foobazrabblim".
    Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A string consisting of lowercase English letters and the characters ( and ). It is 
    guaranteed that all parentheses in inputString form a regular bracket sequence.

    Guaranteed constraints:
    0 ≤ inputString.length ≤ 50.

    [output] string

    Return inputString, with all the characters that were in parentheses reversed.
"""


def reverseInParentheses(s):
    while True:
        temp = []
        control = 0
        for i, ele in enumerate(s):
            if ele == '(':
                if not control:
                    temp.append(i)
                    control = 1
                else:
                    temp.pop()
                    temp.append(i)
            elif ele == ')':
                if control:
                    temp.append(i)
                    control = 0
        if not temp:
            break
        for j in range(0, len(temp), 2):
            s = s[:temp[j]-j] + s[temp[j]+1-j:temp[j+1]-j][::-1] + s[temp[j+1]+1-j:]
    return s                  


print(reverseInParentheses("foo(bar)baz")) #"foorabbaz"
print(reverseInParentheses("foo(bar)baz(blim)")) #"foorabbazmilb"
print(reverseInParentheses("foo(bar(baz))blim")) #"foobazrabblim"
