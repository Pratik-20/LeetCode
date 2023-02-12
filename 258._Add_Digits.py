"""
258. Add Digits

Easy

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
 
"""

# Follow up taken into account so didn't used any loop/recursion

class Solution:
    def addDigits(self, num: int) -> int:
        if num > 9:
            if num % 9 == 0:
                return 9
            else:
                return num % 9
        else:
            return num
 

#Solution 1 - Using while loop

"""

class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            num = str(num)
            sum = 0
            for i in range (0,len(num)):
                sum += int(num[i])
            num = int(sum)

        return(num)
"""


# Solution - Time limit Exeeded Error

"""
class Solution:
    def addDigits(self, num: int) -> int:

        while num not in range(0,9):        # This line is going to consume lot of time # range(0,9)
            num = str(num)
            sum = 0
            for i in range (0,len(num)):
                sum += int(num[i])
            num = int(sum)

        return(num)
"""
