"""
704. Binary Search

Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""


# Binary Search Algorithm.....
# Iterative Solution

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        index = -1

        while begin <= end:
            mid = (begin + end) // 2

            if target == nums[mid]:
                index = mid
                break
            elif target > nums[mid]:
                begin = mid + 1
            elif target < nums[mid]:
                end = mid - 1
        return index


"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        mid = int (len(nums)/2)

        if target == nums[mid]:
            return mid

        elif target > nums[mid]:
            for i in range(mid,len(nums)):
                if nums[i] == target:
                    ans = i
        else:
            for j in range(0,mid):
                if nums[j] == target:
                    ans = j

        return ans


"""

"""

#Simple Python Program.....
# 250 ms

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        for i in range(0,len(nums)):
            if nums[i] == target:
                ans = i
        return ans

"""
