# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-14 01:07:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-14 01:08:38

"""
94. Binary Tree Inorder Traversal Medium
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

Accepted 794,899 Submissions 1,243,548
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    WHITE, RED = 0, 1
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(self.WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == self.WHITE:
                stack.append((self.WHITE, node.right))
                stack.append((self.RED, node))
                stack.append((self.WHITE, node.left))
            else:
                res.append(node.val)
        return res
