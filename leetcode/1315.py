# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-24 21:58:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-24 22:00:35

"""
1315. Sum of Nodes with Even-Valued Grandparent Medium
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
Accepted 51,794 Submissions 61,638
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        queue = [(root, None)]
        while queue:
            a, b = queue.pop()
            flag = False if b is None else b.val >> 1 << 1 == b.val
            if a.left:
                queue.append((a.left, a))
                if flag:
                    res += a.left.val
            if a.right:
                queue.append((a.right, a))
                if flag:
                    res += a.right.val
        return res