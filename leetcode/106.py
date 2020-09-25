# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-25 19:38:08
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-25 19:41:56

"""
106. Construct Binary Tree from Inorder and Postorder Traversal Medium
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
Accepted 254,545 Submissions 531,744
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import bisect


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def decoder(left, right):
            if left > right:
                return None
            val = postorder.pop()
            idx = in2id[val]
            root = TreeNode(val)
            root.right = decoder(idx + 1, right)
            root.left = decoder(left, idx - 1)
            return root

        N = len(inorder)
        if not N:
            return None
        in2id = {jj: ii for ii, jj in enumerate(inorder)}
        return decoder(0, N - 1)
