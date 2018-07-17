
""" digitExpressionTarget
The first 12 digits of pi are 314159265358. We can make these digits into 
an expression evaluating to 27182 (first 5 digits of e) as follows:

3141 * 5 / 9 * 26 / 5 * 3 - 5 * 8 = 27182   
or 
3 + 1 - 415 * 92 + 65358 = 27182

Notice that the order of the input digits is not changed. Operators 
(+,-,/, or *) are simply inserted to create the expression.  

Write a function to take a list of numbers and a target, and return all 
the ways that those numbers can be formed into expressions evaluating to 
the target. Do not use the eval function in Python, Ruby or JavaScript

For example: 
f("314159265358", 27182) should print:      

3 + 1 - 415 * 92 + 65358 = 27182 
3 * 1 + 4 * 159 + 26535 + 8 = 27182 
3 / 1 + 4 * 159 + 26535 + 8 = 27182 
3 * 14 * 15 + 9 + 26535 + 8 = 27182 
3141 * 5 / 9 * 26 / 5 * 3 - 5 * 8 = 27182

################################

"""

# I think this is right, but it is quite slow (I'm not sure if there's a more 
# efficient way to do this) 
def digitExpressionTarget(num, target):
    result, expr, val, i, valStr = [], [], 0, 0, ''
    while i < len(num):
        val = val * 10 + int(num[i])
        valStr += num[i]
        if str(val) != valStr: break
        expr.append(valStr)
        calc(num, target, i+1, 0, val, expr, result)
        expr.pop()
        i += 1
    return result

def calc(num, target, idx, operand1, operand2, expr, result):
    if idx == len(num) and operand1 + operand2 == target:
        result.append(''.join(expr) + ' = ' + str(target))
    else:
        val, i, valStr = 0, idx, ''
        while i < len(num):
            val = val * 10 + int(num[i])
            valStr += num[i]
            if str(val) != valStr: break
            expr.append(' + ' + valStr)
            calc(num, target, i+1, operand1+operand2, val, expr, result)
            expr.pop()
            expr.append(' - ' + valStr)
            calc(num, target, i+1, operand1+operand2, -val, expr, result)
            expr.pop()
            expr.append(' * ' + valStr)
            calc(num, target, i+1, operand1, operand2*val, expr, result)
            expr.pop()
            expr.append(' / ' + valStr)
            calc(num, target, i+1, operand1, operand2/val, expr, result)
            expr.pop()
            i += 1

print(digitExpressionTarget("12365", 26)) # ['1+2+3*6+5', '12+3+6+5']
print(digitExpressionTarget("314159265358", 27182)) # very slow
#print(digitExpressionTarget("12365212354", 26)) # very slow
