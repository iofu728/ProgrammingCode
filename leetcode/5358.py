# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-15 11:09:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-15 11:31:57


"""
5179. Balance a Binary Search Tree
User Accepted:2293
User Tried:2464
Total Accepted:2325
Total Submissions:2937
Difficulty:Medium
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

 

Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.tree = []
        self.Tree2List(root)
        # print(self.tree)
        tree = self.generateBST(self.tree)
        return tree

    def Tree2List(self, root: TreeNode) -> list:
        if root.left != None:
            self.Tree2List(root.left)
        self.tree.append(root.val)
        if root.right != None:
            self.Tree2List(root.right)

    def generateBST(self, tree: list):
        if not len(tree):
            return None
        mid = len(tree) // 2
        root = TreeNode(tree[mid])
        root.left = self.generateBST(tree[:mid])
        root.right = self.generateBST(tree[mid + 1 :])
        return root

