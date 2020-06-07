# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-13 23:08:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-13 23:10:21

"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
通过次数128,137提交次数204,394
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, query, idx = [], [], 1
        if root is None:
            return res
        heapq.heappush(query, (0, 0, root))
        while len(query):
            height, _, front = heapq.heappop(query)
            if len(res) < height + 1:
                res.append([])
            res[height].append(front.val)
            if front.left is not None:
                heapq.heappush(query, (height + 1, idx, front.left))
                idx += 1
            if front.right is not None:
                heapq.heappush(query, (height + 1, idx, front.right))
                idx += 1
        return res
