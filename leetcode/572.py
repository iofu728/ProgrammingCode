# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-08 11:23:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-08 12:33:40

"""
572. 另一个树的子树
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。

通过次数37,616提交次数80,259
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(head, m):
            if head is None:
                return m
            m.append("[{}]".format(head.val))
            if head.left is None:
                m.append("LeftNone")
            else:
                dfs(head.left, m)
            if head.right is None:
                m.append("RightNone")
            else:
                dfs(head.right, m)
            return m

        s = ",".join(dfs(s, []))
        t = ",".join(dfs(t, []))
        return t in s
