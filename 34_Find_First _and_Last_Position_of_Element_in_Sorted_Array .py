"""
34. Find First and Last Position of Element in Sorted Array

Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sett = set(nums)
        if target not in sett:
            return [-1, -1]

        list1 = []  # list to store all positions of target element
        list2 = []  # list to store first and last positions of target element
        # Creating list1 has benefited us if there is only one occurrence of target element

        for i in range(0, len(nums)):
            if nums[i] == target:
                list1.append(i)

        # print(List1)
        list2.append(list1[0])  # insert first position in list2
        list2.append(list1[len(list1) - 1])  # insert second position in list2

        return list2
