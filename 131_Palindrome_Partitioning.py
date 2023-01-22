"""
131. Palindrome Partitioning

Medium


Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_Pali(s):
            return s == s[::-1]

        def backtrack(idx,path,res):

            if idx == len(s):
                res.append(path)
                return

            for i in range(idx,len(s)):

                if is_Pali(s[idx:i+1]):

                    backtrack(i+1,path+[s[idx:i+1]],res)
        res = []
        backtrack(0,[],res)
        return res