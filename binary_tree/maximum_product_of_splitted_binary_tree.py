"""
1339. Maximum Product of Splitted Binary Tree
Medium

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)


Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution:

two max sums of subtrees

If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.

Problems:
- Find the total sum of the tree
- Find the total sum of each subtree
- Compute the max product of two subtrees

- Find the total sum of the tree
    Travese the entire tree and sum each node (iteratively or recursively)

mxSum = None
subTrSums = {}

# Find the total sum of the tree
# Find the total sum of each subtree
def dfs(node):
    if not node:
        return 0
    s = 0
    if node.right:
        s += dfs(node.right)
    if node.left:
        s += dfs(node.left)
    subTrSums[node.val] = node.val + s
    return node.val + s
total_sum = dfs(root)

# Compute the max product of two subtrees
for subtree_sum in subTrSums.values:
    if mxSum:
        mxSum = max(mxSum, (total_sum - subtree_sum) * subtree_sum))
    else:
        mxSum = (total_sum - subtree_sum) * subtree_sum)
return mxSum



"""
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mxSum = None
        subTrSums = {}
        subtree_sum = None
        # Find the total sum of the tree
        # Find the total sum of each subtree
        def dfs(node): # O(n)
            if not node:
                return 0
            s = 0
            if node.right:
                s += dfs(node.right)
            if node.left:
                s += dfs(node.left)

            subTrSums[node] = node.val + s
            return node.val + s



        if not root:
            return None
        total_sum = dfs(root)

        # Compute the max product of two subtrees
        for subtree_sum in subTrSums.values(): # O(n)
            if mxSum:
                mxSum = max(mxSum, (total_sum - subtree_sum) * subtree_sum)
                sub = subtree_sum
            else:
                mxSum = (total_sum - subtree_sum) * subtree_sum
                sub = subtree_sum
        # Runtime: O(n) + O(n) = O(2n) = O(n)
        # Space Complexity: O(n) from the hashmap

        return mxSum % (10**9 + 7)
