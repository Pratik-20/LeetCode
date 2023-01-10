"""
43. Multiply Strings

Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str (eval(num1+ "*" +num2))

"""
Python eval() function parse the expression argument and evaluate it as a python expression and runs python expression (code) within the program.

Python eval() Function Syntax:
Syntax: eval(expression, globals=None, locals=None)

Parameters:

expression: String is parsed and evaluated as a Python expression
globals [optional]: Dictionary to specify the available global methods and variables.
locals [optional]: Another dictionary to specify the available local methods and variables.
Return: Returns output of the expression.
"""
