""" isIPv4Address
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating 
in a computer network that uses the Internet Protocol for communication. There are two versions of 
the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

    For inputString = "172.16.254.1", the output should be
    isIPv4Address(inputString) = true;

    For inputString = "172.316.254.1", the output should be
    isIPv4Address(inputString) = false.

    316 is not in range [0, 255].

    For inputString = ".254.255.0", the output should be
    isIPv4Address(inputString) = false.

    There is no first number.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A string consisting of digits, full stops and lowercase English letters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 30.

    [output] boolean

    true if inputString satisfies the IPv4 address naming rules, false otherwise.
"""


def isIPv4Address(s):
    s_split = s.split('.')
    if len(s_split) != 4:
        return False
    for c in s_split:
        if (not c.isdigit()) or (not 0 <= int(c) <= 255) or (len(c) > 1 and c[0] == '0'):
            return False
    return True


print(isIPv4Address("1.1.1.1a")) # False
print(isIPv4Address("64.233.161.00")) # False
