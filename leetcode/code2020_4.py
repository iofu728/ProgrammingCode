# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-18 15:42:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-18 21:35:41

"""
4. 最小跳跃次数
通过的用户数315
尝试过的用户数1469
用户总通过次数320
用户总提交次数4407
题目难度Hard
为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。若小球在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 i 弹簧处按动弹簧，小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不能再向左弹。

为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。

示例 1：

输入：jump = [2, 5, 1, 1, 1, 1]

输出：3

解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。

限制：

1 <= jump.length <= 10^6
1 <= jump[i] <= 10000
"""
import sys

sys.setrecursionlimit(100000)


class Solution:
    def minJump(self, jump: List[int]) -> int:
        N = len(jump)
        do = [ii + jj for ii, jj in enumerate(jump)]
        do_map, max_do = {}, max(do) + 1

        for ii, jj in enumerate(do):
            if jj not in do_map:
                do_map[jj] = []
            do_map[jj].append(ii)
        self.min_res = 2 ** 32
        # print(do)
        def dfs(res: int, need: int, last_need: int):
            if res >= self.min_res:
                return
            if need == 0:
                if res < self.min_res:
                    self.min_res = res
                return
            out_lists = [
                (ii, jj)
                for ii in range(need, last_need)
                for jj in do_map.get(ii, [])
                if jj < need
            ]
            for ii, jj in out_lists:
                dfs(res + (1 if need == N or ii == need else 2), jj, need)

        dfs(0, N, max_do)
        return self.min_res


# class Solution:
#     def minJump(self, jump: List[int]) -> int:
#         N = len(jump)
#         do = [ii + jj for ii, jj in enumerate(jump)]
#         do_map, max_do = {}, max(do)

#         for ii, jj in enumerate(do):
#             if jj not in do_map:
#                 do_map[jj] = []
#             do_map[jj].append(ii)
#         need, res = N, 0
#         # print(do)
#         while need:
#             if need in do_map:
#                 res += 1
#                 need = do_map[need][0]
#             else:
#                 res += (2 if need != N else 1)
#                 for ii in range(need + 1, max_do + 1):
#                     if ii in do_map:
#                         need = do_map[ii][0]
#                         break
#         return res

from collections import deque  # append(left), pop(left), extend


class Solution:
    def minJump(self, s: List[int]) -> int:
        N = len(s)
        dp = [0] * (N - 1) + [1]
        st = deque([(1, N - 1), (0, N)])
        for i in range(N - 2, -1, -1):
            if i + s[i] >= N:
                dp[i] = 1
                st = deque([(1, i), (0, N)])
            else:
                x = i + s[i]
                l, r = 0, len(st) - 1
                while l + 1 < r:
                    mi = (l + r) // 2
                    if st[mi][1] > x:
                        r = mi
                    else:
                        l = mi
                print(st, l)
                now = min(dp[x], st[l][0] + 1) + 1
                dp[i] = now
                while st[0][0] > dp[i]:
                    st.popleft()
                st.appendleft((dp[i], i))
        print(dp)
        return dp[0]
