# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-09 10:20:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-09 10:21:31

"""
1079. Letter Tile Possibilities Medium
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
Accepted 34,641 Submissions 45,961
"""
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def getC(a, b):
            ans = 1
            if b > a // 2:
                b = a - b
            for ii in range(a, a - b, -1):
                ans *= ii
            for ii in range(2, b + 1):
                ans /= ii
            return int(ans)

        def dfs(idx: int, last_num: int, now: dict):
            total = sum(now.values())
            if total and last_num:
                ans = 1
                for ii in now.values():
                    # print(total, ii, getC(total, ii))
                    ans *= getC(total, ii)
                    total -= ii
                self.res += ans
            else:
                ans = 0
            # print(ans, idx, now)
            if idx > N - 1:
                return
            for jj in range(c_y[idx] + 1):
                if jj:
                    now[c_x[idx]] = jj
                dfs(idx + 1, jj, now)
                if jj:
                    del now[c_x[idx]]

        c = Counter(tiles)
        c_x = list(c.keys())
        c_y = list(c.values())
        N = len(c_x)
        # print(N)
        self.res = 0
        dfs(0, 0, {})
        return self.res
