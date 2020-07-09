# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-08 00:33:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-08 00:34:32

"""
112. Path Sum
Easy

1877

490

Add to List

Share
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Accepted
471,195
Submissions
1,152,598
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        queue = []
        if root is None:
            return False
        idx = 0
        heapq.heappush(queue, (-1, 0, root.val, root))
        while len(queue):
            _, hight, t_sum, head = heapq.heappop(queue)
            if head.left is None and head.right is None:
                if t_sum == sum:
                    return True
            if head.left:
                heapq.heappush(
                    queue, (idx, hight + 1, t_sum + head.left.val, head.left)
                )
                idx += 1
            if head.right:
                heapq.heappush(
                    queue, (idx, hight + 1, t_sum + head.right.val, head.right)
                )
                idx += 1
        return False

