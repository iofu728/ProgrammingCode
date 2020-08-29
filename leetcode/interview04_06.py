# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 18:03:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 18:03:35

"""
面试题 04.06. 后继者
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:

输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
示例 2:

输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

输出: null
通过次数8,140提交次数13,927
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res, stack = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root)
            root = root.right
        res.append(None)
        for ii in range(len(res)):
            if res[ii] == p:
                return res[ii + 1]
        return None
