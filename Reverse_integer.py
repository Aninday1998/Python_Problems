'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1
'''



class Solution:
    def reversed(self, x: int) -> int:
        if (x >= 0):
            a = int(str(x)[::-1])
        else:
            a = int('-' + str(x)[1:][::-1])
        if (a in range(pow(-2, 31), pow(2, 31))):
            return a
        else:
            return 0

s = Solution()
p = s.reversed(320)
print(p)