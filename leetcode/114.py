# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-02 00:25:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-02 00:26:26

"""
144. Binary Tree Preorder Traversal Medium
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

Accepted 506,529 Submissions 911,624
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(head: TreeNode):
            if head is None:
                return
            lists.append(head)
            dfs(head.left)
            dfs(head.right)

        lists = []
        dfs(root)
        N = len(lists)
        for ii in range(1, N):
            prev, now = lists[ii - 1], lists[ii]
            prev.left = None
            prev.right = now

