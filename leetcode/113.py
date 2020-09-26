# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-26 00:36:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-26 00:38:14

"""
113. Path Sum II Medium
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
Accepted 354,479 Submissions 747,909
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        queue, idx, res = [], 1, []
        if root is None:
            return []
        heapq.heappush(queue, (0, 0, root, [root.val], root.val))
        while queue:
            _, h, head, tmp, tmp_s = heapq.heappop(queue)
            # print(tmp_s, tmp)
            if head.left is None and head.right is None:
                if tmp_s == sum:
                    res.append(tmp)
                continue
            if head.left:
                heapq.heappush(
                    queue,
                    (
                        idx,
                        h + 1,
                        head.left,
                        tmp + [head.left.val],
                        tmp_s + head.left.val,
                    ),
                )
                idx += 1
            if head.right:
                heapq.heappush(
                    queue,
                    (
                        idx,
                        h + 1,
                        head.right,
                        tmp + [head.right.val],
                        tmp_s + head.right.val,
                    ),
                )
                idx += 1
        return res
