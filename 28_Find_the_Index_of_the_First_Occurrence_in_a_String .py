"""
28. Find the Index of the First Occurrence in a String

Medium

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

# Solution

"""haystack = "adbutads"
needle = "sad"

for i in range (0,len(haystack)):
    if haystack[i] == needle[0]:
        if haystack[i:i+len(needle)] == needle:
            print(i)
            exit()
    if i== len(haystack)-1 and haystack[i] != needle:
            print("-1")
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                # if first letter is equal then and then only check for word
                if haystack[i:i + len(needle)] == needle:
                    return i

            if i == len(haystack) - 1 and haystack[i] != needle:
                # if needle is not found in the end of haystack then return -1
                # condition and added after and is usefull in the case if needle lkenth is 1
                return -1
