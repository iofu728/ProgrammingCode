# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-20 19:20:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-20 19:20:50

"""
1007. Minimum Domino Rotations For Equal Row
Medium

1986

223

Add to List

Share
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
Accepted
156,675
Submissions
303,000
"""


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        c = Counter(tops + bottoms)
        k = max(c.items(), key=lambda i: (i[1]))
        if k[1] < N:
            return -1
        res, y = 0, 0
        for ii, jj in zip(tops, bottoms):
            if k[0] not in [ii, jj]:
                return -1
            res += int(ii != k[0])
            y += int(jj != k[0])
        return min(res, y)