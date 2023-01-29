"""
6339. 将珠子放入背包中 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Hard
你有 k 个背包。给你一个下标从 0 开始的整数数组 weights ，其中 weights[i] 是第 i 个珠子的重量。同时给你整数 k 。

请你按照如下规则将所有的珠子放进 k 个背包。

没有背包是空的。
如果第 i 个珠子和第 j 个珠子在同一个背包里，那么下标在 i 到 j 之间的所有珠子都必须在这同一个背包中。
如果一个背包有下标从 i 到 j 的所有珠子，那么这个背包的价格是 weights[i] + weights[j] 。
一个珠子分配方案的 分数 是所有 k 个背包的价格之和。

请你返回所有分配方案中，最大分数 与 最小分数 的 差值 为多少。

 

示例 1：

输入：weights = [1,3,5,1], k = 2
输出：4
解释：
分配方案 [1],[3,5,1] 得到最小得分 (1+1) + (3+1) = 6 。
分配方案 [1,3],[5,1] 得到最大得分 (1+3) + (5+1) = 10 。
所以差值为 10 - 6 = 4 。
示例 2：

输入：weights = [1, 3], k = 2
输出：0
解释：唯一的分配方案为 [1],[3] 。
最大最小得分相等，所以返回 0 。
 

提示：

1 <= k <= weights.length <= 105
1 <= weights[i] <= 109
"""
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        res = weights[0] + weights[-1]
        ka = []
        for ii in range(N - 1):
            heapq.heappush(ka, weights[ii] + weights[ii + 1])
            if len(ka) > k - 1:
                heapq.heappop(ka)
        res += sum(ka)
        y = weights[0] + weights[-1]
        ka = []
        for ii in range(N - 1):
            heapq.heappush(ka, -weights[ii] - weights[ii + 1])
            if len(ka) > k - 1:
                heapq.heappop(ka)
        y -= sum(ka)
        return res - y