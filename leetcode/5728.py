# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-11 11:32:33
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-11 11:32:45
"""
5728. 最少侧跳次数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个长度为 n 的 3 跑道道路 ，它总共包含 n + 1 个 点 ，编号为 0 到 n 。一只青蛙从 0 号点第二条跑道 出发 ，它想要跳到点 n 处。然而道路上可能有一些障碍。

给你一个长度为 n + 1 的数组 obstacles ，其中 obstacles[i] （取值范围从 0 到 3）表示在点 i 处的 obstacles[i] 跑道上有一个障碍。如果 obstacles[i] == 0 ，那么点 i 处没有障碍。任何一个点的三条跑道中 最多有一个 障碍。

比方说，如果 obstacles[2] == 1 ，那么说明在点 2 处跑道 1 有障碍。
这只青蛙从点 i 跳到点 i + 1 且跑道不变的前提是点 i + 1 的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在 同一个 点处 侧跳 到 另外一条 跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。

比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。
这只青蛙从点 0 处跑道 2 出发，并想到达点 n 处的 任一跑道 ，请你返回 最少侧跳次数 。

注意：点 0 处和点 n 处的任一跑道都不会有障碍。

 

示例 1：


输入：obstacles = [0,1,2,3,0]
输出：2 
解释：最优方案如上图箭头所示。总共有 2 次侧跳（红色箭头）。
注意，这只青蛙只有当侧跳时才可以跳过障碍（如上图点 2 处所示）。
示例 2：


输入：obstacles = [0,1,1,3,3,0]
输出：0
解释：跑道 2 没有任何障碍，所以不需要任何侧跳。
示例 3：


输入：obstacles = [0,2,1,0,3,0]
输出：2
解释：最优方案如上图所示。总共有 2 次侧跳。
 

提示：

obstacles.length == n + 1
1 <= n <= 5 * 105
0 <= obstacles[i] <= 3
obstacles[0] == obstacles[n] == 0
"""


class Solution:
    MAX = 10 ** 9 + 7

    def minSideJumps(self, o: List[int]) -> int:
        N = len(o)
        dp, new = [1] * 3, [0] * 3
        dp[1] = 0
        for ii in range(1, N):
            if o[ii] != 0:
                can_go = [jj for jj in range(3) if jj != o[ii] - 1]
                dp[o[ii] - 1] = self.MAX
            else:
                can_go = range(3)
            new = dp.copy()
            for jj in can_go:
                new[jj] = min([dp[kk] if kk == jj else dp[kk] + 1 for kk in range(3)])
            # print(dp, new)
            dp, new = new, [0] * 3
        return min(dp)
