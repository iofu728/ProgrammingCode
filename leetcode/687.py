# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-05-03 10:57:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-05-03 10:57:28

"""
687. 最长同值路径
给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度 由它们之间的边数表示。

 

示例 1:



输入：root = [5,4,5,1,1,5]
输出：2
示例 2:



输入：root = [1,4,5,4,4,5]
输出：2
 

提示:

树的节点数的范围是 [0, 104] 
-1000 <= Node.val <= 1000
树的深度将不超过 1000 
通过次数44,758提交次数99,770
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(h):
            if h is None:
                return 0
            l = dfs(h.left)
            r = dfs(h.right)
            if h.left is None or h.val != h.left.val:
                l = 0
            if h.right is None or h.val != h.right.val:
                r = 0
            self.res = max(l + r, self.res)
            return max(l, r) + 1
        self.res = 0
        dfs(root)
        return self.res
