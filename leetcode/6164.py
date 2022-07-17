# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-17 11:22:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-17 11:23:06

"""
6164. 数位和相等数对的最大和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。请你选出两个下标 i 和 j（i != j），且 nums[i] 的数位和 与  nums[j] 的数位和相等。

请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。

 

示例 1：

输入：nums = [18,43,36,13,7]
输出：54
解释：满足条件的数对 (i, j) 为：
- (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。
- (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。
所以可以获得的最大和是 54 。
示例 2：

输入：nums = [10,12,19,14]
输出：-1
解释：不存在满足条件的数对，返回 -1 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_k(n):
            res = 0
            while n > 0:
                res += n % 10
                n //= 10
            return res
        c = defaultdict(list)
        for ii in nums:
            heapq.heappush(c[get_k(ii)], ii)
            if len(c[get_k(ii)]) > 2:
                heapq.heappop(c[get_k(ii)])
        res = -1
        for ii, jj in c.items():
            if len(jj) >= 2:
                res = max(res, sum(jj))
        return res
        