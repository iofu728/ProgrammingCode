# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 19:49:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 19:50:48

"""
701. Insert into a Binary Search Tree Medium
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
 

Constraints:

The number of nodes in the given tree will be between 0 and 10^4.
Each node will have a unique integer value from 0 to -10^8, inclusive.
-10^8 <= val <= 10^8
It's guaranteed that val does not exist in the original BST.
Accepted 122,339 Submissions 158,737
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MAX = 10 ** 9 + 7

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(head: TreeNode, left: int, right: int):
            if head is None:
                return
            print(head.val, left, right)
            if self.flag:
                return
            if head.left is None and head.right is None:
                if left < val < head.val:
                    head.left = TreeNode(val)
                    self.flag = True
                elif head.val < val < right:
                    head.right = TreeNode(val)
                    self.flag = True
            if head.left:
                dfs(head.left, left, head.val)
            elif left < val < head.val:
                head.left = TreeNode(val)
                self.flag = True

            if head.right:
                dfs(head.right, head.val, right)
            elif head.val < val < right:
                head.right = TreeNode(val)
                self.flag = True

        if root is None:
            return TreeNode(val)
        self.flag = False
        dfs(root, -self.MAX, self.MAX)
        return root
