# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-25 13:00:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-25 13:10:31

"""
230. Kth Smallest Element in a BST Medium

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

## Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

## Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

## Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

## Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Accepted 313,749 Submissions 557,071
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []

        def infix_order(head: TreeNode):
            if head.left is not None:
                infix_order(head.left)
            if len(result) > k:
                return
            result.append(head.val)
            if head.right is not None:
                infix_order(head.right)

        infix_order(root)
        return result[k - 1]
