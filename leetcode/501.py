# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-24 19:50:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-24 19:52:52

"""
501. Find Mode in Binary Search Tree Easy
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

Accepted 91,793 Submissions 215,237
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(head: TreeNode):
            nonlocal tmp, tmp_t, res_t, res
            if head is None:
                return
            dfs(head.left)
            if head.val == tmp:
                tmp_t += 1
            else:
                tmp = head.val
                tmp_t = 1
            if tmp_t > res_t:
                res, res_t = [tmp], tmp_t
            elif tmp_t == res_t:
                res.append(tmp)
            dfs(head.right)

        res, res_t = [], 0
        tmp, tmp_t = 0, 0
        dfs(root)
        return res
