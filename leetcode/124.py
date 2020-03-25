# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-25 22:48:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-25 23:02:47

"""
124. Binary Tree Maximum Path Sum Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

## Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

## Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
Accepted 284,539 Submissions 876,200
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -999999

        def pathSum(r: TreeNode):
            if r is None:
                return 0
            val = r.val
            left = max(pathSum(r.left), 0)
            right = max(pathSum(r.right), 0)
            self.ans = max(self.ans, left + right + val)
            return max(left, right) + val

        pathSum(root)
        return self.ans
