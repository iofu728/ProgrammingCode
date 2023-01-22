# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-01-22 12:23:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-01-22 12:23:25

"""
6299. 拆分数组的最小代价 显示英文描述 
通过的用户数406
尝试过的用户数681
用户总通过次数553
用户总提交次数1386
题目难度Hard
给你一个整数数组 nums 和一个整数 k 。

将数组拆分成一些非空子数组。拆分的 代价 是每个子数组中的 重要性 之和。

令 trimmed(subarray) 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。

例如，trimmed([3,1,2,4,3,4]) = [3,4,3,4] 。
子数组的 重要性 定义为 k + trimmed(subarray).length 。

例如，如果一个子数组是 [1,2,3,3,3,4,4] ，trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4] 。这个子数组的重要性就是 k + 5 。
找出并返回拆分 nums 的所有可行方案中的最小代价。

子数组 是数组的一个连续 非空 元素序列。

 

示例 1：

输入：nums = [1,2,1,2,1,3,3], k = 2
输出：8
解释：将 nums 拆分成两个子数组：[1,2], [1,2,1,3,3]
[1,2] 的重要性是 2 + (0) = 2 。
[1,2,1,3,3] 的重要性是 2 + (2 + 2) = 6 。
拆分的代价是 2 + 6 = 8 ，可以证明这是所有可行的拆分方案中的最小代价。
示例 2：

输入：nums = [1,2,1,2,1], k = 2
输出：6
解释：将 nums 拆分成两个子数组：[1,2], [1,2,1] 。
[1,2] 的重要性是 2 + (0) = 2 。
[1,2,1] 的重要性是 2 + (2) = 4 。
拆分的代价是 2 + 4 = 6 ，可以证明这是所有可行的拆分方案中的最小代价。
示例 3：

输入：nums = [1,2,1,2,1], k = 5
输出：10
解释：将 nums 拆分成一个子数组：[1,2,1,2,1].
[1,2,1,2,1] 的重要性是 5 + (3 + 2) = 10 。
拆分的代价是 10 ，可以证明这是所有可行的拆分方案中的最小代价。
 

提示：

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
1 <= k <= 109

"""
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        # def get_num(a, x):
        #     return 0 if a - (x - 1) == 1 else a - (x - 1)
        # C = Counter(nums)
        # c = Counter(C.values())
        # print(c)
        # res = float("inf")
        # for x in range(1, max(c.keys())):
        #     tmp = sum(get_num(a, x) * b for a, b in c.items()) + k * x
        #     print(x, k * x, sum(get_num(a, x) * b for a, b in c.items()))
        #     res = min(tmp, res)
        #     c = {a : b for a, b in c.items() if a <= x}
        # return res
        
#         C = defaultdict(int)
#         cs = [C.copy()]
        
#         for ii in nums:
#             C[ii] += 1
#             cs.append(C.copy())
#         # print(1)
            
#         @lru_cache(None)
#         def dfs(l, r):
#             X = {k: cs[r][k] - cs[l][k] for k in cs[r].keys() if cs[r][k] != cs[l][k]}
#             c = Counter(X.values())
#             res = k + sum(a * b for a, b in c.items() if a > 1)
#             single = 0
#             b = 0
#             p = 0
#             for x in range(l + 1, r):
#                 if cs[x][nums[x - 1]] - cs[l][nums[x - 1]] == 1 and cs[r][nums[x - 1]] - cs[l][nums[x - 1]] != 1:
#                     single += 1
#                     b += 1
#                 if cs[r][nums[x - 1]] - cs[x][nums[x - 1]] == 1 and cs[r][nums[x - 1]] - cs[l][nums[x - 1]] != 1:
#                     single += 1
#                 if cs[x][nums[x - 1]] - cs[l][nums[x - 1]] == 2:
#                     single -= 1
#                     b -= 1
#                 if cs[r][nums[x - 1]] - cs[x][nums[x - 1]] == 0 and cs[r][nums[x - 1]] - cs[l][nums[x - 1]] != 1:
#                     single -= 1
#                 if single >= k:
#                     # if dfs(l, x) + dfs(x, r) < res:
#                     #     p = x
#                         # print(single)
#                     # res = min(res, k + x - l - b + dfs(x, r))
#                     res = min(res, (dfs(l, x) if x - l > k else k + x - l) + dfs(x, r))
#             # if p != 0:
#             #     print(p)
                    
#             return res
#         return dfs(0, len(nums))

        N = len(nums)

        @lru_cache(None)
        def dfs(x):
            if x == N:
                return 0
            res = k + N - x
            c = defaultdict(int)
            tmp = 0
            for ii in range(x, N):
                num = nums[ii]
                c[num] += 1
                if c[num] == 2:
                    tmp += 2
                elif c[num] > 2:
                    tmp += 1
                res = min(res, tmp + k + dfs(ii + 1))
            return res
            
        return dfs(0)
            
            