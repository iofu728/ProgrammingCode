# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-23 22:56:04
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-23 22:56:39

"""
298. 二叉树最长连续序列
给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。

该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。

这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。

示例 1：

输入:

   1
    \
     3
    / \
   2   4
        \
         5

输出: 3

解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3
示例 2：

输入:

   2
    \
     3
    / 
   2    
  / 
 1

输出: 2 

解析: 当中，最长连续序列是 2-3。注意，不是 3-2-1，所以返回 2。
通过次数2,692提交次数4,806
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(now: TreeNode, pre_l: int, pre_v: int):
            if now is None:
                return
            if now.val == pre_v + 1 or pre_l == 0:
                pre_l += 1
                if pre_l > self.res:
                    self.res = pre_l
            else:
                pre_l = 1
            pre_v = now.val
            dfs(now.left, pre_l, pre_v)
            dfs(now.right, pre_l, pre_v)

        self.res = 0
        dfs(root, 0, 0)
        return self.res
