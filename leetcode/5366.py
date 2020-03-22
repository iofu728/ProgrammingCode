# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 10:45:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 11:23:16

"""
5366. Check if There is a Valid Path in a Grid
User Accepted:706
User Tried:1047
Total Accepted:715
Total Submissions:1690
Difficulty:Medium
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directors = [(3, 1), (0, 2), (3, 2), (2, 1), (0, 3), (0, 1)]
        idx_change = [2, 3, 0, 1]
        idx_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        M, N = len(grid), len(grid[0])
        self.flag = False
        have_gone = set()
        # print(M, N)
        pos_x, pos_y, director = 0, 0, 1
        while pos_x < M and pos_y < N and pos_x >= 0 and pos_y >= 0:
            if tuple([pos_x, pos_y]) in have_gone:
                self.flag = False
                break
            have_gone.add(tuple([pos_x, pos_y]))
            director = idx_change[director]
            dir_x, dir_y = directors[grid[pos_x][pos_y] - 1]
            # print(dir_x, dir_y)
            if [pos_x, pos_y] != [0, 0] and dir_x != director and dir_y != director:
                self.flag = False
                break
            if pos_x == M - 1 and pos_y == N - 1:
                self.flag = True
                # print(1, self.flag)
                break
            if [pos_x, pos_y] == [0, 0]:
                if dir_x in [1, 2]:
                    dir_x, dir_y = dir_y, dir_x
            elif dir_y == director:
                dir_x, dir_y = dir_y, dir_x
            change_x, change_y = idx_dir[dir_y]
            pos_x += change_x
            pos_y += change_y
            director = dir_y
        return self.flag
            
            
            