"""
547. Number of Provinces
Medium

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

"""
Solution:

[1,1,0],
[1,1,0],
[0,0,1]

[1,0,0],
[0,1,0],
[0,0,1]

[1,0,0,1],
[0,1,1,0],
[0,1,1,1],
[1,0,1,1]

How do I sum up all of the provinces?
How do I determine if a group of cells is a province?

provinces = 0
nNodes = len(isConnected)
seen = [False]*nNodes


def dfs(n):
    if not seen[node]:
        seen[node] = True
        for con in isConnected[node]:
            # 0 eval as false
            if isConnected[node][con]:
                return dfs(con)


for node in range(len(isConnected)):
    if not seen[node]:
        dfs(node)
        provinces += 1

def dfs(i, j):
    if (i, j) in seen:
        return 0
    seen.add((i, j))
    return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

Runtime: O(n * m) where n is the number of rows and m is the number of columns in the matrix
Space Complexity: O(n)
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        nNodes = len(isConnected)
        seen = [False]*nNodes


        def dfs(n):
            if not seen[n]:
                seen[n] = True
                for con in range(nNodes):
                    # 0 eval as false
                    if isConnected[n][con]:
                        dfs(con)


        for i in range(nNodes):
            if not seen[i]:
                dfs(i)
                provinces += 1
        return provinces
