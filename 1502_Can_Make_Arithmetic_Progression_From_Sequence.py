"""
1502. Can Make Arithmetic Progression From Sequence

Easy
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:

2 <= arr.length <= 1000
-106 <= arr[i] <= 106

"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        list = []
        for i in range(1, len(arr)):
            list.append(arr[i] - (arr[i - 1]))

        # print(list)
        # print(set(list))
        list2 = []
        for j in set(list):
            list2.append(j)
        # print(len(list2))
        if len(list2) == 1:
            return True
        else:
            return False

