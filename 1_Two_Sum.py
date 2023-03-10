"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

# Solution ---

# Run any code -
# Code - 1
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                a = nums[i] + nums[j]
                if i != j:
                    if a == target:
                        return(i,j)
                        exit()
                    else:
                        pass

"""
# Code - 2
# Drawback of this code is it gives error as -  "Time Limit Exceeded"

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                a = nums[i] + nums[j]
                if i != j:
                    if a == target:
                        answer.append(i)
                        answer.append(j)
                        return answer
                        exit()
                    else:
                        pass
#"""
