# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-22 00:43:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-22 00:43:04

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(head: TreeNode):
            if head is None:
                return [float("inf"), 0, 0]
            la, lb, lc = dfs(head.left)
            ra, rb, rc = dfs(head.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]

        a, b, c = dfs(root)
        return b
