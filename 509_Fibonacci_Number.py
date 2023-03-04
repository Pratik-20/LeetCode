"""
509. Fibonacci Number

Easy

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:

0 <= n <= 30
"""

"""

# Solution 1 - Using Recursion

# Consumes much time more than 650m 
class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            return(f(n-1) + f(n-2))                 
        return f(n)
"""

"""
# Solution 1 - Just inserted else condition..
class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:                                   #Just used else
                return(f(n-1) + f(n-2))                 
        return f(n)
"""


#"""
# Solution 2 : - Main Solution Using Dynamic Programming

# Just consume littel bit time Hardly 27ms ++

class Solution:
    def fib(self, n: int) -> int:
        dp_array = [0,1]
        def f(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n <= len(dp_array):
                return dp_array[n-1]
            else:
                dp_array.append(f(n-1) + f(n-2))
                return dp_array[n-1]
        return f(n)
#"""


"""
# Solution 3 : - Using Backtracking

# Just consume littel bit time Hardly 25ms ++



class Solution:
    def fib(self, n: int) -> int:
        def f(n, memo={}):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            elif n in memo:
                return memo[n]
            else:
                memo[n] = f(n-1) + f(n-2)
                return memo[n]

        # Driver Program
        return(f(n))

"""
