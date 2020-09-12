# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-12 00:37:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-12 00:38:54

"""
637. Average of Levels in Binary Tree Easy
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
Accepted 134,661 Submissions 212,427
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res, tmp, queue = [], [], []
        idx, pre = 1, 0
        heapq.heappush(queue, (0, 0, root))
        while queue:
            _, h, head = heapq.heappop(queue)
            if h == pre:
                tmp.append(head.val)
            else:
                if tmp:
                    res.append(sum(tmp) / len(tmp))
                tmp = [head.val]
                pre = h
            if head.left:
                heapq.heappush(queue, (idx, h + 1, head.left))
                idx += 1
            if head.right:
                heapq.heappush(queue, (idx, h + 1, head.right))
                idx += 1
        if tmp:
            res.append(sum(tmp) / len(tmp))
        return res
