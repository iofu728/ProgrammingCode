# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-22 13:03:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-22 13:16:36

"""
199. Binary Tree Right Side View Medium
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
Accepted 253,275 Submissions 483,544
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res, queue, idx = {}, [], 1
        heapq.heappush(queue, (0, 0, root))
        while len(queue):
            layer, _, head = heapq.heappop(queue)
            if head is None:
                break
            res[layer] = head.val
            # print(head.val, layer)
            if not head.left is None:
                heapq.heappush(queue, (layer + 1, idx, head.left))
                idx += 1
            if not head.right is None:
                heapq.heappush(queue, (layer + 1, idx, head.right))
                idx += 1
        return list(res.values())
