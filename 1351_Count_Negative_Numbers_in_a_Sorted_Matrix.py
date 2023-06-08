
"""

1351. Count Negative Numbers in a Sorted Matrix

Easy

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of
negative numbers in grid.

Example
1:

Input: grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example
2:

Input: grid = [[3, 2], [1, 0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] < 0:
                    # print(grid[i][j])
                    count += 1
        return count
