# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-26 10:37:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-26 11:00:39

"""
5474. 好叶子节点对的数量 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你二叉树的根节点 root 和一个整数 distance 。

如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。

返回树中 好叶子节点对的数量 。

示例 1：

输入：root = [1,2,3,null,4], distance = 3
输出：1
解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。
示例 2：

输入：root = [1,2,3,4,5,6,7], distance = 3
输出：2
解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。
示例 3：

输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
输出：1
解释：唯一的好叶子节点对是 [2,5] 。
示例 4：

输入：root = [100], distance = 1
输出：0
示例 5：

输入：root = [1,1,1], distance = 2
输出：1
 

提示：

tree 的节点数在 [1, 2^10] 范围内。
每个节点的值都在 [1, 100] 之间。
1 <= distance <= 10
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        subTrees = []
        self.idx = 0

        def getSeries(head, before):
            now = "{}#{}".format(before, self.idx)
            self.idx += 1
            if not head.left and not head.right:
                subTrees.append(now)
                return
            if head.left:
                getSeries(head.left, now)
            if head.right:
                getSeries(head.right, now)

        def getDiff(a, b):
            a, b = a.split("#"), b.split("#")
            idx = 0
            aa, bb = len(a), len(b)
            while idx < aa and idx < bb and a[idx] == b[idx]:
                idx += 1
            return (aa - idx) + (bb - idx)

        res = 0
        getSeries(root, "")
        # print(subTrees)
        M = len(subTrees)
        for idx in range(M):
            for jdx in range(idx + 1, M):

                if getDiff(subTrees[idx], subTrees[jdx]) <= distance:
                    res += 1
        return res

