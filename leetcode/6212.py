"""
6216. 使数组相等的最小开销 显示英文描述 
通过的用户数64
尝试过的用户数79
用户总通过次数64
用户总提交次数95
题目难度Hard
给你两个下标从 0 开始的数组 nums 和 cost ，分别包含 n 个 正 整数。

你可以执行下面操作 任意 次：

将 nums 中 任意 元素增加或者减小 1 。
对第 i 个元素执行一次操作的开销是 cost[i] 。

请你返回使 nums 中所有元素 相等 的 最少 总开销。

 

示例 1：

输入：nums = [1,3,5,2], cost = [2,3,1,14]
输出：8
解释：我们可以执行以下操作使所有元素变为 2 ：
- 增加第 0 个元素 1 次，开销为 2 。
- 减小第 1 个元素 1 次，开销为 3 。
- 减小第 2 个元素 3 次，开销为 1 + 1 + 1 = 3 。
总开销为 2 + 3 + 3 = 8 。
这是最小开销。
示例 2：

输入：nums = [2,2,2,2,2], cost = [4,2,8,1,3]
输出：0
解释：数组中所有元素已经全部相等，不需要执行额外的操作。
 

提示：

n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106
"""
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        res = inf
        N = len(nums)
        c = set(nums)
        # nc = sorted(zip(nums, cost), key=lambda i:(-i[1], i[0]))
        last, last_idx, pre, total = None, None, 0, sum(cost)
        ka = defaultdict(int)
        for ii, jj in zip(nums, cost):
            ka[ii] += jj
        for l in sorted(c):
            now = ka[l]
            if last is None:
                tmp = sum([abs(ii - l) * jj for ii, jj in ka.items()])
                res = min(tmp, res)
            else:
                y = total - pre
                # print(last, y, l - last_idx, pre)
                tmp = last - y * (l - last_idx) + pre * (l - last_idx)
                res = min(tmp, res)
            
            if last and tmp > last:
                break
            last = tmp
            pre += now
            last_idx = l
        return res
                
            
                
            
            