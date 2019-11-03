""" addBinary
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,2) + int(b,2)))[2:]


print(Solution().addBinary("11", "1")) #100
print(Solution().addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
"110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011")) 
#"110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"


'''alternative: slower, more complicated

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0 
        result = ['0' for x in range(len(a)+1 if len(a)>=len(b) else len(b)+1)]
        for i in range(1, len(result)+1):
            tempA = int(a[-i]) if (len(a))-i >= 0 else 0
            tempB = int(b[-i]) if (len(b))-i >= 0 else 0
            temp = tempA + tempB + carry
            if temp == 3:
                result[-i] = '1'
                carry = 1
            elif temp == 2:
                result[-i] = '0'
                carry = 1
            elif temp == 1:
                result[-i] = '1'
                carry = 0
            else:
                result[-i] = '0'
                carry = 0
        return ''.join(result) if result[0] != '0' else ''.join(result)[1:]
'''
            
