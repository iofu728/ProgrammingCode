# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-25 13:43:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-25 14:17:15

"""
892. Surface Area of 3D Shapes Easy

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

## Example 1:
Input: [[2]]
Output: 10

## Example 2:
Input: [[1,2],[3,4]]
Output: 34

## Example 3:
Input: [[1,0],[0,2]]
Output: 16

## Example 4:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

## Example 5:
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

## Note:
1 <= N <= 50
0 <= grid[i][j] <= 50

Accepted 16,167 Submissions 27,847
"""


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        b, cover = 0, 0
        for ii in range(N):
            for jj in range(N):
                t = grid[ii][jj]
                b += t
                cover += t - 1 if t > 1 else 0
                if ii:
                    cover += min(grid[ii - 1][jj], t)
                if jj:
                    cover += min(grid[ii][jj - 1], t)
        return 6 * b - 2 * cover
