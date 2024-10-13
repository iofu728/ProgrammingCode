# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-10-13 12:03:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-10-13 12:03:54

"""
100373. K-th Largest Perfect Subtree Size in Binary Tree
User Accepted:62
User Tried:81
Total Accepted:62
Total Submissions:92
Difficulty:Medium
You are given the root of a binary tree and an integer k.

Return an integer denoting the size of the kth largest perfect binary subtree, or -1 if it doesn't exist.

A perfect binary tree is a tree where all leaves are on the same level, and every parent has two children.

A subtree of treeName is a tree consisting of a node in treeName and all of its descendants.

 

Example 1:

Input: root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2

Output: 3

Explanation:



The roots of the perfect binary subtrees are highlighted in black. Their sizes, in decreasing order are [3, 3, 1, 1, 1, 1, 1, 1].
The 2nd largest size is 3.

Example 2:

Input: root = [1,2,3,4,5,6,7], k = 1

Output: 7

Explanation:



The sizes of the perfect binary subtrees in decreasing order are [7, 3, 3, 1, 1, 1, 1]. The size of the largest perfect binary subtree is 7.

Example 3:

Input: root = [1,2,3,null,4], k = 3

Output: -1

Explanation:



The sizes of the perfect binary subtrees in decreasing order are [1, 1]. There are fewer than 3 perfect binary subtrees.

 

Constraints:

The number of nodes in the tree is in the range [1, 2000].
1 <= Node.val <= 2000
1 <= k <= 1024
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        def get_x(r):
            if r is None:
                return 0
            left = get_x(r.left)
            right = get_x(r.right)
            if left == right and left != -1:
                res.append(2 ** (left + 1) - 1)
                return left + 1
            return -1
        res = []
        get_x(root)
        res = sorted(res, reverse=True)
        # print(res)
        
        return res[k - 1] if len(res) > k - 1 else -1
        