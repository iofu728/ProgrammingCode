# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-05-02 12:06:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-05-02 12:06:59

"""
5748. 包含每个查询的最小区间 显示英文描述 
通过的用户数73
尝试过的用户数291
用户总通过次数74
用户总提交次数476
题目难度Hard
给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示第 i 个区间开始于 lefti 、结束于 righti（包含两侧取值，闭区间）。区间的 长度 定义为区间中包含的整数数目，更正式地表达是 righti - lefti + 1 。

再给你一个整数数组 queries 。第 j 个查询的答案是满足 lefti <= queries[j] <= righti 的 长度最小区间 i 的长度 。如果不存在这样的区间，那么答案是 -1 。

以数组形式返回对应查询的所有答案。

 

示例 1：

输入：intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
输出：[3,3,1,4]
解释：查询处理如下：
- Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。
- Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。
示例 2：

输入：intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
输出：[2,-1,4,6]
解释：查询处理如下：
- Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。
- Query = 19：不存在包含 19 的区间，答案为 -1 。
- Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。
- Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。
 

提示：

1 <= intervals.length <= 105
1 <= queries.length <= 105
queries[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107
"""
import bisect


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        nums = [jj for ii in intervals for jj in ii]
        MIN, MAX = min(nums), max(nums)
        dp, dp_map = [], {}
        for ii, jj in sorted(intervals, key=lambda i: -(i[1] - i[0])):
            left = bisect.bisect_left(dp, ii)
            right = bisect.bisect_left(dp, jj)
            gap = 0
            # print(ii, jj)
            for kk in range(max(left - 1, 0), min(right + 1, len(dp))):
                # print(kk - gap)
                begin = dp[kk - gap]
                end, h = dp_map[begin]
                if end < ii or begin > jj:
                    continue
                if begin >= ii:
                    dp.pop(kk - gap)
                    gap += 1
                if end > jj:
                    # print("###")
                    x = jj + 1
                    dp_map[x] = [end, h]
                    bisect.insort(dp, x)
                if begin < ii:
                    # print("***")
                    y = ii - 1
                    dp_map[begin] = [min(end, y), h]
            bisect.insort(dp, ii)
            dp_map[ii] = [jj, jj - ii + 1]
            # print(dp, dp_map)
        # print(dp)
        # print(dp_map)
        res = []
        for ii in queries:
            left = bisect.bisect_left(dp, ii)
            if not (left < len(dp) and dp[left] == ii):
                left = max(left - 1, 0)
            if left >= len(dp):
                res.append(-1)
                continue
            begin = dp[left]
            end, h = dp_map[begin]
            if begin <= ii <= end:
                res.append(h)
            else:
                res.append(-1)
        return res