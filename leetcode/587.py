# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-28 12:57:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-28 12:58:10

"""
587. Erect the Fence Hard
There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

Example 1:

Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:

Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them. 
 

Note:

All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.
input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
Accepted 9,692 Submissions 27,022
"""
from collections import Counter


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def getLineDist(a: list, b: list, c: list):
            return (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])

        def isBetween(a: list, c: list, b: list):
            aa = b[0] >= c[0] >= a[0] or b[0] <= c[0] <= a[0]
            bb = b[1] >= c[1] >= a[1] or b[1] <= c[1] <= a[1]
            return aa and bb

        res, N, times, left_most = set(), len(points), 0, 0
        if N <= 4:
            return points
        for ii in range(N):
            if points[ii][0] < points[left_most][0]:
                left_most = ii
        p = left_most

        while p != left_most or times == 0:
            q = (p + 1) % N
            for ii in range(N):
                if ii in [p, q]:
                    continue
                if getLineDist(points[p], points[ii], points[q]) < 0:
                    q = ii

            for ii in range(N):
                if ii in [p, q]:
                    continue
                if getLineDist(points[p], points[ii], points[q]) == 0 and isBetween(
                    points[p], points[ii], points[q]
                ):
                    # print(points[p], points[ii], points[q])
                    res.add(tuple(points[ii]))
            res.add(tuple(points[q]))
            p = q
            times += 1

        return [list(ii) for ii in res]
