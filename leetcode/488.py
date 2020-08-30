# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 15:31:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 15:31:45

"""
488. Zuma Game Hard
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 
Example 4:

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 
 

Constraints:

You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
1 <= board.length <= 16
1 <= hand.length <= 5
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
Accepted 14,123 Submissions 35,470
"""
from collections import Counter


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def decoder(pss: list, ii: int):
            N = len(pss)
            left, right = ii - 1, ii + 1
            while left >= 0 and right < N and pss[left][1] == pss[right][1]:
                size, w = pss[right]
                size = pss[left][0] + size
                if size >= 3:
                    left -= 1
                    right += 1
                else:
                    right += 1
                    pss[left] = (size, w)
            # print(pss, ii, left, right)
            return pss[: left + 1] + pss[right:]

        def dfs(ps: list, c: dict):
            # print(ps, c)
            if total - sum(c.values()) > self.res:
                return
            if not len(ps):
                self.res = min(total - sum(c.values()), self.res)
                return
            for ii in range(len(ps)):
                size, w = ps[ii]
                need = 3 - size
                if w not in c or c[w] < need:
                    continue
                c[w] -= need
                dfs(decoder(ps, ii), c)
                c[w] += need
            for ii in range(len(ps)):
                size, w = ps[ii]
                if size != 2:
                    continue
                for k, v in c.items():
                    if k == w or v <= 0:
                        continue
                    for t in range(1, 2):
                        if t > v:
                            continue
                        c[k] -= t
                        dfs(ps[:ii] + [(1, w), (t, k), (1, w)] + ps[ii + 1 :], c)
                        c[k] += t

        N = len(board)
        hand_c = Counter(hand)
        # print(hand_c)
        total = len(hand)
        self.res = 10 ** 9 + 7
        for k, v in Counter(board).items():
            if v % 3 == 0:
                continue
            if k not in hand_c or hand_c[k] + v < 3:
                # print(k, v, hand_c[k])
                return -1
        b = [0] + [ii for ii in range(1, N) if board[ii] != board[ii - 1]]
        e = [ii for ii in range(N - 1) if board[ii] != board[ii + 1]] + [N - 1]
        pairs = [(jj - ii + 1, board[ii]) for ii, jj in zip(b, e)]
        dfs(pairs, hand_c)
        return -1 if self.res == 10 ** 9 + 7 else self.res
