# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-30 11:53:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-30 11:53:43

"""
100358. 找出有效子序列的最大长度 II 显示英文描述 
通过的用户数2
尝试过的用户数3
用户总通过次数2
用户总提交次数3
题目难度Medium
给你一个整数数组 nums 和一个 正 整数 k 。
nums 的一个 子序列 sub 的长度为 x ，如果其满足以下条件，则称其为 有效子序列 ：

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k
返回 nums 的 最长有效子序列 的长度。
 

示例 1：

输入：nums = [1,2,3,4,5], k = 2

输出：5

解释：

最长有效子序列是 [1, 2, 3, 4, 5] 。

示例 2：

输入：nums = [1,4,2,3,1,4], k = 3

输出：4

解释：

最长有效子序列是 [1, 4, 1, 4] 。

 

提示：

2 <= nums.length <= 103
1 <= nums[i] <= 107
1 <= k <= 103

"""
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums = [ii % k for ii in nums]
        N = len(nums)
        c = Counter(nums)
        res = max(c.values())

        c = defaultdict(int)
        d = defaultdict(int)

        for ii in nums:
            for jj in c.keys():
                if jj == ii:
                    continue
                d[(jj, ii)] = d[(ii, jj)] + 1
            c[ii] += 1
        return max(res, max(d.values()) + 1 if len(d) else 0)