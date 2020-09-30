# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 20:17:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 20:17:45

"""
剑指 Offer 12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/

通过次数57,729提交次数129,427
"""


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, flag: list, pre: str):
            if not word.startswith(pre):
                return
            if word == pre:
                self.res = True
                return
            if self.res:
                return
            for dx, dy in self.DIRS:
                xx, yy = dx + x, dy + y
                if not (0 <= xx < N) or not (0 <= yy < M) or flag[xx][yy] == 0:
                    continue
                flag[xx][yy] = 0
                dfs(xx, yy, flag, pre + board[xx][yy])
                flag[xx][yy] = 1

        N, M = len(board), len(board[0])
        self.res = False
        flag = [[1] * M for _ in range(N)]
        for ii in range(N):
            for jj in range(M):
                if board[ii][jj] == word[0]:
                    flag[ii][jj] = 0
                    dfs(ii, jj, flag, board[ii][jj])
                    flag[ii][jj] = 1
        return self.res
