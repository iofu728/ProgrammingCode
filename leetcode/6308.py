# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-03-05 12:26:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-03-05 12:26:57


"""
6308. 二叉树中的第 K 大层和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一棵二叉树的根节点 root 和一个正整数 k 。

树中的 层和 是指 同一层 上节点值的总和。

返回树中第 k 大的层和（不一定不同）。如果树少于 k 层，则返回 -1 。

注意，如果两个节点与根节点的距离相同，则认为它们在同一层。

 

示例 1：



输入：root = [5,8,9,2,1,3,7,4,6], k = 2
输出：13
解释：树中每一层的层和分别是：
- Level 1: 5
- Level 2: 8 + 9 = 17
- Level 3: 2 + 1 + 3 + 7 = 13
- Level 4: 4 + 6 = 10
第 2 大的层和等于 13 。
示例 2：



输入：root = [1,2,null,3], k = 1
输出：3
解释：最大的层和是 3 。
 

提示：

树中的节点数为 n
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        d = defaultdict(int)
        q = [(0, 0, root)]
        res = []
        m = 0
        idx = 0
        while q:
            h, _, now = heapq.heappop(q)
            if now is None:
                continue
            d[h] += now.val
            if h > m:
                m = h
                heapq.heappush(res, d[h - 1])
                if len(res) > k:
                    heapq.heappop(res)
            if now.left:
                idx += 1
                heapq.heappush(q, (h + 1, idx, now.left))
            if now.right:
                idx += 1
                heapq.heappush(q, (h + 1, idx, now.right))
        heapq.heappush(res, d[m])
        if len(res) > k:
            heapq.heappop(res)
        return heapq.heappop(res) if len(res) >= k else -1
