# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-29 19:53:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-29 19:56:35

"""
145. Binary Tree Postorder Traversal Medium
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [2,1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?

Accepted 411,254 Submissions 737,498
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    WRITE, RED = 0, 1

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(self.WRITE, root)]
        while stack:
            flag, head = stack.pop()
            if head is None:
                continue
            if flag == self.WRITE:
                stack.append((self.RED, head))
                stack.append((self.WRITE, head.right))
                stack.append((self.WRITE, head.left))
            else:
                res.append(head.val)
            # print(stack)
        return res
