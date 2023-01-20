"""
491. Non-decreasing Subsequences

Medium


Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with
at least two elements. You may return the answer in any order.



Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]


Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100

"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        final_result = set()

        def task(nums, indexx, path):

            if len(path) >= 2:
                final_result.add(tuple(path))
            for i in range(indexx, len(nums)):
                if not path or nums[i] >= path[-1]:  # using Stack Approach to check increasing order
                    # https://www.geeksforgeeks.org/python-check-if-list-is-strictly-increasing/
                    # 5th method from this page
                    task(nums, i + 1, path + [nums[i]])

        task(nums, 0, [])

        return list(final_result)
