# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-16 09:37:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-16 09:38:47

"""
226. Invert Binary Tree Easy
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
Accepted 572,892 Submissions 875,624
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        tmp, queue, idx = root, [], 0
        heapq.heappush(queue, (0, 0, root))
        while queue:
            _, h, head = heapq.heappop(queue)
            head.left, head.right = head.right, head.left
            if head.left:
                heapq.heappush(queue, (idx, h + 1, head.left))
                idx += 1
            if head.right:
                heapq.heappush(queue, (idx, h + 1, head.right))
                idx += 1
        return root
