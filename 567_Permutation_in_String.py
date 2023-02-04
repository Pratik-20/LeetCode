"""
567. Permutation in String

Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

# Solution 1
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        status = False
        list1 = []
        for i in range (0,len(s1)):
            list1.append(s1[i])
        list1 = sorted(list1)
        list2 = []

        for j in range(0,len(s2)):
            #print(s2[j])
            if s2[j] in list1:
                for k in range(j,(j+len(s1))):
                    try:
                        list2.append(s2[k])
                    except IndexError:
                        return False
                list2 = sorted(list2)
                if list2 == list1:
                    status = True
                    return True
                    exit()
                else:
                    list2 = []
        return status
"""


# Solution 2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)  # Example: s1 = "abi"  s2 = "eidbiaoo"
        # ctr1 = {b:2, a:1, i:1}
        ctr1, ctr2 = Counter(s1), Counter(s2[:n1])
        #  i     ctr2                  ctr1 == ctr2
        for i in range(n1, n2):  # ––––   –––––––––––––––       ––––––––––––
            if ctr1 == ctr2: return True  # 4     {e:1, i:1, d:1, b:1}      False
            #  5     {b:2, i:1, d:1}           False
            ctr2[s2[i - n1]] -= 1  # 6     {b:2, a:1, i:1}           True
            ctr2[s2[i]] += 1

        return ctr1 == ctr2
