# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-26 00:48:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-26 00:49:31

"""
773. Sliding Puzzle Hard
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
Accepted 44,024 Submissions 73,362
"""


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        N, M = len(board), len(board[0])
        target = list(range(1, 6)) + [0]
        head = [jj for ii in board for jj in ii]
        seen = {tuple(head)}
        queue = [(head, head.index(0), 0)]
        while queue:
            now, idx, h = queue.pop(0)
            if now == target:
                return h
            for dx in (1, -1, M, -M):
                new_idx = idx + dx
                if abs(new_idx // M - idx // M) + abs(
                    new_idx % M - idx % M
                ) != 1 or not (0 <= new_idx < N * M):
                    continue
                tmp = now.copy()
                tmp[new_idx], tmp[idx] = tmp[idx], tmp[new_idx]
                if tuple(tmp) not in seen:
                    seen.add(tuple(tmp))
                    queue.append((tmp, new_idx, h + 1))
        return -1
