"""
1657. Determine if Two Strings Are Close

Medium

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
"""




class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        chars_1 = set(word1)
        chars_2 = set(word2)

        count_1 = [word1.count(chr) for chr in chars_1]
        count_2 = [word2.count(chr) for chr in chars_2]

        return len(word1) == len(word2) and chars_1 == chars_2 and sorted(count_1) == sorted(count_2)
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        else:
            chars_1 = set(word1)
            chars_2 = set(word2)

            count_1 = [word1.count(chr) for chr in chars_1]
            count_2 = [word2.count(chr) for chr in chars_2]

            return len(word1) == len(word2) and chars_1 == chars_2 and sorted(count_1) == sorted(count_2)

"""

"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        else:
            count_1 = [0] * 26
            count_2 = [0] * 26

            for char in word1:
                count_1[ord(char) - ord('a')] += 1

            for char in word2:
                count_2[ord(char) - ord('a')] += 1

            for i in range(26):
                if (count_1[i] == 0 and count_2[i] != 0) or (count_2[i] != 0 and count_1[i] == 0):
                    return False

            count_1 = sorted(count_1)
            count_2 = sorted(count_2)

            for i in range(26):
                if count_1[i] != count_2[i]:
                    return False
            return True
"""

