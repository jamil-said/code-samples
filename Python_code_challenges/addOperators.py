
"""
 Given a string that contains only digits 0-9 and a target value, return 
 all possibilities to add binary operators (not unary) +, -, or * between 
 the digits so they evaluate to the target value.

Examples:

"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

"""

class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result, expr, val, i, valStr = [], [], 0, 0, ''
        while i < len(num):
            val = val * 10 + int(num[i])
            valStr += num[i]
            if str(val) != valStr: break
            expr.append(valStr)
            self.calc(num, target, i+1, 0, val, expr, result)
            expr.pop()
            i += 1
        return result

    def calc(self, num, target, pos, operand1, operand2, expr, result):
        if pos == len(num) and operand1 + operand2 == target:
            result.append(''.join(expr))
        else:
            val, i, valStr = 0, pos, ''
            while i < len(num):
                val = val * 10 + int(num[i])
                valStr += num[i]
                if str(val) != valStr: break
                expr.append('+' + valStr)
                self.calc(num, target, i+1, operand1+operand2, val, expr, result)
                expr.pop()
                expr.append('-' + valStr)
                self.calc(num, target, i+1, operand1+operand2, -val, expr, result)
                expr.pop()
                expr.append('*' + valStr)
                self.calc(num, target, i+1, operand1, operand2*val, expr, result)
                expr.pop()
                i += 1



