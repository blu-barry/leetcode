"""
695. Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""
"""
Solution:

seen = set()
dfs(i, j)
    if i < 0 or j < 0 or i >= len(area) or j >= len(area[0]) or (i, j) in seen or area[i][j] == 0:
        return 0
    seen.add((i, j))
    s = 0
    s += dfs(i+1, j)
    s += dfs(i-1, j)
    s += dfs(i, j+1)
    s += dfs(i, j-1)
    return 1+s

Iterate over rows
    Iterate over columns
        if value is > 0 and not seen:
            mx = max(mx, dfs(index of value))

Runtime:
    visiting every node once, O(n * m ) where n is the width and m is the height
Space Complexity:
    O(n), for the seen set()
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        mx = 0
        width, height = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= width or j >= height or (i, j) in seen or grid[i][j] == 0:
                return 0
            seen.add((i, j))
            s = 0
            s += dfs(i+1, j)
            s += dfs(i-1, j)
            s += dfs(i, j+1)
            s += dfs(i, j-1)
            return s + 1

        for i in range(width):
            for j in range(height):
                if (i, j) not in seen:
                    if grid[i][j] > 0:
                        mx = max(mx, dfs(i, j))
        return mx
