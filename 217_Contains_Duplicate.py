"""
217. Contains Duplicate

Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


# Simple way to solve this problem is to test the size of list with the set made up from the list
# Using this method will be really helpful to reduce operation time
# Running for loop could be more time consuming and bit complex

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_1 = list(set(nums))      # Create a set from list
        if len(set_1) != len(nums):  # Check the length of Set with list
            return True              # if not same size then obviously there is Duplicate
        else:
            return False             # if same size then there no Duplicate
