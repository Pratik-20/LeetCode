"""
66. Plus One

Easy

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


# Solution 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        for i in digits:
            a += str(i)
        b = int(a) + 1
        c = []
        for j in str(b):
            c.append(int(j))
        return c


# Solution 2
"""            
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str(int(''.join([str(x) for x in digits])) + 1)]
"""
