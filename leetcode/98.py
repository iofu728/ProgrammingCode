# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-26 20:39:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-26 20:52:54

"""
98. Validate Binary Search Tree Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

## Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

## Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
Accepted 602,948 Submissions 2,216,910
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        MAX_NUM = 2 ** 32 - 1
        self.result = True

        def validOnce(head: TreeNode, lower: int, upper: int) -> bool:
            if self.result == False:
                return False
            if head is None:
                return True
            if head.val >= upper or head.val <= lower:
                self.result = False
                return False
            return validOnce(head.left, lower, head.val) and validOnce(
                head.right, head.val, upper
            )

        validOnce(root, -MAX_NUM, MAX_NUM)
        return self.result
