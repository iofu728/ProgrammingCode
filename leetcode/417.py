"""
417. Pacific Atlantic Water Flow
Medium

3549

807

Add to List

Share
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
Accepted
195,460
Submissions
398,049
"""


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(starts):
            q = deque(starts)
            flag = set(starts)
            while q:
                x, y = q.popleft()
                for dx, dy in self.DIRS:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < N and 0 <= yy < M and heights[xx][yy] >= heights[x][y] and (xx, yy) not in flag:
                        q.append((xx, yy))
                        flag.add((xx, yy))
            return flag

        N, M = len(heights), len(heights[0])
        a = [(0, ii) for ii in range(M)] + [(ii, 0) for ii in range(1, N)]
        b = [(N - 1, ii) for ii in range(M)] + [(ii, M - 1)
                                                for ii in range(N - 1)]
        # print(a)
        # print(b)
        return list(bfs(a) & bfs(b))
