# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-05 23:24:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 00:13:53

"""
5494. 统计所有可行路径 显示英文描述 
通过的用户数268
尝试过的用户数327
用户总通过次数279
用户总提交次数469
题目难度Hard
给你一个 互不相同 的整数数组，其中 locations[i] 表示第 i 个城市的位置。同时给你 start，finish 和 fuel 分别表示出发城市、目的地城市和你初始拥有的汽油总量

每一步中，如果你在城市 i ，你可以选择任意一个城市 j ，满足  j != i 且 0 <= j < locations.length ，并移动到城市 j 。从城市 i 移动到 j 消耗的汽油量为 |locations[i] - locations[j]|，|x| 表示 x 的绝对值。

请注意， fuel 任何时刻都 不能 为负，且你 可以 经过任意城市超过一次（包括 start 和 finish ）。

请你返回从 start 到 finish 所有可能路径的数目。

由于答案可能很大， 请将它对 10^9 + 7 取余后返回。

 

示例 1：

输入：locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
输出：4
解释：以下为所有可能路径，每一条都用了 5 单位的汽油：
1 -> 3
1 -> 2 -> 3
1 -> 4 -> 3
1 -> 4 -> 2 -> 3
示例 2：

输入：locations = [4,3,1], start = 1, finish = 0, fuel = 6
输出：5
解释：以下为所有可能的路径：
1 -> 0，使用汽油量为 fuel = 1
1 -> 2 -> 0，使用汽油量为 fuel = 5
1 -> 2 -> 1 -> 0，使用汽油量为 fuel = 5
1 -> 0 -> 1 -> 0，使用汽油量为 fuel = 3
1 -> 0 -> 1 -> 0 -> 1 -> 0，使用汽油量为 fuel = 5
示例 3：

输入：locations = [5,2,1], start = 0, finish = 2, fuel = 3
输出：0
解释：没有办法只用 3 单位的汽油从 0 到达 2 。因为最短路径需要 4 单位的汽油。
示例 4 ：

输入：locations = [2,1,5], start = 0, finish = 0, fuel = 3
输出：2
解释：总共有两条可行路径，0 和 0 -> 1 -> 0 。
示例 5：

输入：locations = [1,2,3], start = 0, finish = 2, fuel = 40
输出：615088286
解释：路径总数为 2615088300 。将结果对 10^9 + 7 取余，得到 615088286 。
 

提示：

2 <= locations.length <= 100
1 <= locations[i] <= 10^9
所有 locations 中的整数 互不相同 。
0 <= start, finish < locations.length
1 <= fuel <= 200
"""
sys.setrecursionlimit(100000)

from functools import lru_cache


class Solution:
    MODS = 10 ** 9 + 7

    def countRoutes(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        @lru_cache(None)
        def dfs(now: int, oil: int):
            ans = 0
            for ii, loc in enumerate(locations):
                if now == ii:
                    continue
                cost = abs(locations[now] - loc)
                if cost <= oil:
                    ans += dfs(ii, oil - cost)
            if now == finish:
                ans += 1
            return ans % self.MODS

        return dfs(start, fuel)

