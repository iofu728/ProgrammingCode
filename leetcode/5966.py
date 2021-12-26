# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-12-26 11:18:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-12-26 11:18:26

"""
5966. 还原原数组 显示英文描述 
User Accepted:34
User Tried:54
Total Accepted:34
Total Submissions:76
Difficulty:Hard
Alice 有一个下标从 0 开始的数组 arr ，由 n 个正整数组成。她会选择一个任意的 正整数 k 并按下述方式创建两个下标从 0 开始的新整数数组 lower 和 higher ：

对每个满足 0 <= i < n 的下标 i ，lower[i] = arr[i] - k
对每个满足 0 <= i < n 的下标 i ，higher[i] = arr[i] + k
不幸地是，Alice 丢失了全部三个数组。但是，她记住了在数组 lower 和 higher 中出现的整数，但不知道每个整数属于哪个数组。请你帮助 Alice 还原原数组。

给你一个由 2n 个整数组成的整数数组 nums ，其中 恰好 n 个整数出现在 lower ，剩下的出现在 higher ，还原并返回 原数组 arr 。如果出现答案不唯一的情况，返回 任一 有效数组。

注意：生成的测试用例保证存在 至少一个 有效数组 arr 。

 

示例 1：

输入：nums = [2,10,6,4,8,12]
输出：[3,7,11]
解释：
如果 arr = [3,7,11] 且 k = 1 ，那么 lower = [2,6,10] 且 higher = [4,8,12] 。
组合 lower 和 higher 得到 [2,6,10,4,8,12] ，这是 nums 的一个排列。
另一个有效的数组是 arr = [5,7,9] 且 k = 3 。在这种情况下，lower = [2,4,6] 且 higher = [8,10,12] 。
示例 2：

输入：nums = [1,1,3,3]
输出：[2,2]
解释：
如果 arr = [2,2] 且 k = 1 ，那么 lower = [1,1] 且 higher = [3,3] 。
组合 lower 和 higher 得到 [1,1,3,3] ，这是 nums 的一个排列。
注意，数组不能是 [1,3] ，因为在这种情况下，获得 [1,1,3,3] 唯一可行的方案是 k = 0 。
这种方案是无效的，k 必须是一个正整数。
示例 3：

输入：nums = [5,435]
输出：[220]
解释：
唯一可行的组合是 arr = [220] 且 k = 215 。在这种情况下，lower = [5] 且 higher = [435] 。
 

提示：

2 * n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 109
生成的测试用例保证存在 至少一个 有效数组 arr
"""
from collections import Counter
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        def dfs(k):
            res = []
            nk = Counter([])
            for ii in nums:
                jj = ii + 2 * k
                if n_sets[ii] == nk[ii]:
                    continue
                if jj in n_sets and n_sets[jj] > nk[jj]:
                    res.append(ii + k)
                    nk[ii] += 1
                    nk[jj] += 1
                else:
                    return False
            return res
                    
        
        nums = sorted(nums)
        N = len(nums) // 2
        poss = set()
        n_sets = Counter(nums)
        n_set = list(n_sets.keys())
        M = len(n_set)
        if M == 1:
            return [n_set[0]] * N
        for ii in range(1, M):
            tmp = abs(n_set[ii] - n_set[0])
            if tmp > 0 and tmp >> 1 << 1 == tmp:
                poss.add(tmp // 2)
        # print(poss, n_sets, nums)
        for k in poss:
            tmp = dfs(k)
            if tmp:
                return tmp
        return []
