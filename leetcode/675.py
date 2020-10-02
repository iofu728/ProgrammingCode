# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-02 18:46:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-02 18:46:59

"""
675. Cut Off Trees for Golf Event Hard
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
In one step you can walk in any of the four directions top, bottom, left and right also when standing in a point which is a tree you can decide whether or not to cut off the tree.

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

Constraints:

1 <= forest.length <= 50
1 <= forest[i].length <= 50
0 <= forest[i][j] <= 10^9
Accepted 35,400 Submissions 101,953
"""


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(sx, sy, tx, ty):
            # print(sx, sy, tx, ty)
            queue = collections.deque([(sx, sy, 0)])
            seen = {(sx, sy)}
            while queue:

                x, y, d = queue.popleft()
                # print(x, y, d)
                if x == tx and y == ty:
                    return d
                for dx, dy in self.DIRS:
                    xx, yy = x + dx, y + dy
                    if (
                        not (0 <= xx < N)
                        or not (0 <= yy < M)
                        or not forest[xx][yy]
                        or (xx, yy) in seen
                    ):
                        continue
                    seen.add((xx, yy))
                    queue.append((xx, yy, d + 1))
            return -1

        N, M = len(forest), len(forest[0])
        trees = sorted(
            [
                (forest[ii][jj], ii, jj)
                for ii in range(N)
                for jj in range(M)
                if forest[ii][jj]
            ]
        )
        sx, sy = 0, 0
        res = 0
        for _, tx, ty in trees:
            d = bfs(sx, sy, tx, ty)
            if d == -1:
                return -1
            res += d
            sx, sy = tx, ty
        return res
