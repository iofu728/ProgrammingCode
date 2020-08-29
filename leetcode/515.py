# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 18:21:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 18:22:33

"""
515. Find Largest Value in Each Tree Row Medium
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []
 

Constraints:

The number of the nodes in the tree will be in the range [1, 104].
-231 <= Node.val <= 231 - 1
Accepted 107,277 Submissions 175,291
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        idx, res, queue = 1, {}, []
        heapq.heappush(queue, (0, 0, root))
        while queue:
            _, h, front = heapq.heappop(queue)
            if h not in res:
                res[h] = front.val
            else:
                res[h] = max(res[h], front.val)
            if front.left:
                heapq.heappush(queue, (idx, h + 1, front.left))
                idx += 1
            if front.right:
                heapq.heappush(queue, (idx, h + 1, front.right))
                idx += 1
        return [res[ii] for ii in sorted(res)]

