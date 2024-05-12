# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-12 12:05:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-12 12:05:44

"""
100312. 找出分数最低的排列 显示英文描述 
通过的用户数1
尝试过的用户数6
用户总通过次数1
用户总提交次数6
题目难度Hard
给你一个数组 nums ，它是 [0, 1, 2, ..., n - 1] 的一个排列 。对于任意一个 [0, 1, 2, ..., n - 1] 的排列 perm ，其 分数 定义为：

score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|

返回具有 最低 分数的排列 perm 。如果存在多个满足题意且分数相等的排列，则返回其中字典序最小的一个。

 

示例 1：

输入：nums = [1,0,2]

输出：[0,1,2]

解释：



字典序最小且分数最低的排列是 [0,1,2]。这个排列的分数是 |0 - 0| + |1 - 2| + |2 - 1| = 2 。

示例 2：

输入：nums = [0,2,1]

输出：[0,2,1]

解释：



字典序最小且分数最低的排列是 [0,2,1]。这个排列的分数是 |0 - 1| + |2 - 2| + |1 - 0| = 2 。

 

提示：

2 <= n == nums.length <= 14
nums 是 [0, 1, 2, ..., n - 1] 的一个排列。
"""
from functools import lru_cache
from typing import List


class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        @lru_cache(None)
        def helper(end, remain, cnt):
            if cnt == 1:
                idx = 0
                while remain > 1:
                    remain >>= 1
                    idx += 1
                return abs(end - nums[idx]) + abs(idx - nums[0]), (idx, )
            tmp = 99999
            best = None
            for i in range(1, n):
                if remain & (1 << i):
                    value, li = helper(i, remain - (1 << i), cnt - 1)
                    now = abs(end - nums[i]) + value
                    if now < tmp:
                        tmp = now
                        best = i, li
            return tmp, best

        ans = helper(0, (1 << n) - 2, n - 1)[1]
        res = [0]
        while len(ans) == 2:
            res.append(ans[0])
            ans = ans[1]
        res.append(ans[0])
        return res
