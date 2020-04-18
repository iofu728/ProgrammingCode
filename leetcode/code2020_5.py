# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-18 21:35:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-18 21:36:50


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def dfs(x):
    if not x.left and not x.right:
        return x.val, 0
    if not x.left:
        a, b = dfs(x.right)
        return a + x.val, b
    if not x.right:
        a, b = dfs(x.left)
        return a + x.val, b
    a, b = x.val, 0
    c, d = dfs(x.left)
    e, f = dfs(x.right)
    b += d + f
    if c < e:
        c, d, e, f = e, f, c, d
    b += e
    c -= e
    if c <= f + f:
        b += c / 2
    else:
        b += f
        a += c - f * 2
    return a, b


class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        a, b = dfs(root)
        return a + b
