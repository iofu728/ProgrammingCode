# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-25 14:16:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-25 14:19:26

"""
655. Print Binary Tree Medium
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].

Accepted 32,383 Submissions 59,005
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getMaxDepth(h: TreeNode):
            if not h:
                return 0
            left = getMaxDepth(h.left)
            right = getMaxDepth(h.right)
            return max(left, right) + 1

        depth = getMaxDepth(root)
        res = [[""] * (2 ** depth - 1) for _ in range(depth)]
        queue, idx = [], 1
        heapq.heappush(queue, (0, 0, 0, 2 ** depth - 1, root))
        while len(queue):
            _, height, left, right, head = heapq.heappop(queue)
            res[height][(left + right) // 2] = str(head.val)
            if head.left:
                heapq.heappush(
                    queue, (idx, height + 1, left, (left + right) // 2, head.left)
                )
                idx += 1
            if head.right:
                heapq.heappush(
                    queue, (idx, height + 1, (left + right) // 2, right, head.right)
                )
                idx += 1
        return res

