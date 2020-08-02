# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-02 17:24:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-02 17:25:10

"""
1457. Pseudo-Palindromic Paths in a Binary Tree Medium
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:

Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1

Constraints:

The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.
Accepted 15,539 Submissions 23,142
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
import heapq


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def is_palindromic(a: list):
            co = Counter(a)
            flag = False
            for k, v in co.items():
                if v >> 1 << 1 != v:
                    if flag:
                        return False
                    flag = True
            return True

        res, queue, idx = 0, [], 1
        if not root:
            return 0
        heapq.heappush(queue, (0, [root.val], root))
        while len(queue):
            _, pre, head = heapq.heappop(queue)
            if not head.left and not head.right:
                if is_palindromic(pre):
                    res += 1
            if head.left:
                heapq.heappush(queue, (idx, pre + [head.left.val], head.left))
                idx += 1
            if head.right:
                heapq.heappush(queue, (idx, pre + [head.right.val], head.right))
                idx += 1
        return res

