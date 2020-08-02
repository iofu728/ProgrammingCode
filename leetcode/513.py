# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-02 16:01:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-02 16:02:29

"""
513. Find Bottom Left Tree Value Medium
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.

Accepted 106,708 Submissions 173,732
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res, queue, idx = [], [], 1
        MAX_H = -1
        heapq.heappush(queue, (0, 0, root))
        while len(queue):
            _, height, head = heapq.heappop(queue)
            if height != MAX_H:
                res = []
                MAX_H = height
                res.append(head.val)
            if head.left:
                heapq.heappush(queue, (idx, height + 1, head.left))
                idx += 1
            if head.right:
                heapq.heappush(queue, (idx, height + 1, head.right))
                idx += 1
        return res[0]

