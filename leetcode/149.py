# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-02 23:49:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-02 23:51:20

"""
149. Max Points on a Line Hard
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Accepted 159,530 Submissions 938,474
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            if b != 0:
                return gcd(b, a % b)
            return a

        N = len(points)
        if N <= 2:
            return N
        dp = [0] * N
        res = 2
        for ii in range(N):
            tmp = {}
            c_d, h_l = 0, 1
            for jj in range(ii + 1, N):
                a, b = points[ii], points[jj]
                if a[0] == b[0] and a[1] == b[1]:
                    c_d += 1
                elif a[1] == b[1]:
                    h_l += 1
                else:
                    k = gcd(a[0] - b[0], a[1] - b[1])
                    dx = (a[0] - b[0]) // k
                    dy = (a[1] - b[1]) // k
                    k = "{}/{}".format(dx, dy)
                    tmp[k] = tmp.get(k, 1) + 1
            tmp_v = max(tmp.values()) if len(tmp) else 0
            now = max(h_l, tmp_v) + c_d
            res = max(res, now)
        return res
