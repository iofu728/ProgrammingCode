# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-09 23:09:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-09 23:10:56

"""
1372. Longest ZigZag Path in a Binary Tree Medium
Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right then move to the right child of the current node otherwise move to the left child.
Change the direction from right to left or right to left.
Repeat the second and third step until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0

Constraints:

Each tree has at most 50000 nodes..
Each node's value is between [1, 100].
Accepted 9,773 Submissions 18,223
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        l, r = defaultdict(int), defaultdict(int)
        if root is None:
            return 0
        q = deque([(root, None)])
        while len(q):
            node, parent = q.popleft()
            if parent:
                if parent.left == node:
                    l[node] = r[parent] + 1
                else:
                    r[node] = l[parent] + 1
            if node.left:
                q.append((node.left, node))
            if node.right:
                q.append((node.right, node))
        return max(max(l.values()) if len(l) else 0, max(r.values()) if len(r) else 0)
