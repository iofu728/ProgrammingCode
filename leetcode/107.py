# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-06 00:35:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 00:35:44

"""
107. Binary Tree Level Order Traversal II Easy
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
Accepted
367,558 Submissions 683,332
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res, queue, idx = [], [], 1
        heapq.heappush(queue, (idx, 0, root))
        if root is None:
            return []
        while queue:
            _, h, head = heapq.heappop(queue)
            if len(res) < h + 1:
                res.append([])
            res[h].append(head.val)
            if head.left:
                heapq.heappush(queue, (idx, h + 1, head.left))
                idx += 1
            if head.right:
                heapq.heappush(queue, (idx, h + 1, head.right))
                idx += 1
        return res[::-1]
