# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-19 16:45:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-19 16:58:19

"""
404. Sum of Left Leaves Easy
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
Accepted 213,135 Submissions 409,878
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(head, father: int):
            nonlocal res
            if head is None or head.left is None and head.right is None:
                if father == 1:
                    res += head.val
                return
            if head.left:
                dfs(head.left, 1)
            if head.right:
                dfs(head.right, 2)
                
        res = 0

        dfs(root, 0)
        return res
