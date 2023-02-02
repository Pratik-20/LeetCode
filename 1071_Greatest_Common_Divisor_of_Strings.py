"""
1071. Greatest Common Divisor of Strings

Easy

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters
"""

# Requirement Math + String
# Math = Euclidean's Algorithm - https://youtu.be/yHwneN6zJmU


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = len(str1)
        b = len(str2)

        # list1 = []                                    # Store q,a,b,r as per each stage
        # list2 = []                                    # Store q,a,b,r at current stage
        list3 = []
        w = ""

        def ram(a, b):
            # list2 = []
            # print("Ais = ", a)
            list3.append(a)
            if b != 0:
                r = a % b
                # print("R is = ", r)
                q = (a - r) / b
                """
                #print("B is = ", b)
                list2.append(q)
                list2.append(a)
                list2.append(b)
                list2.append(r)
                list1.append(list2)
                print("r is", r)"""

                ram(a=b, b=r)

        ram(a, b)

        z = list3[-1]
        y = len(str1) / z
        x = len(str2) / z
        if set(str1) == set(str2):
            print(z)
            if str2[:z] * int(x) == str2:
                if str2[:z] * int(y) == str1:
                    w = str2[:z]

        return (w)

