# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-19 11:38:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-19 11:38:33

"""
100300. 所有数对中数位不同之和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
车尔尼有一个数组 nums ，它只包含 正 整数，所有正整数的数位长度都 相同 。

两个整数的 数位不同 指的是两个整数 相同 位置上不同数字的数目。

请车尔尼返回 nums 中 所有 整数对里，数位不同之和。

 

示例 1：

输入：nums = [13,23,12]

输出：4

解释：
计算过程如下：
- 13 和 23 的数位不同为 1 。
- 13 和 12 的数位不同为 1 。
- 23 和 12 的数位不同为 2 。
所以所有整数数对的数位不同之和为 1 + 1 + 2 = 4 。

示例 2：

输入：nums = [10,10,10,10]

输出：0

解释：
数组中所有整数都相同，所以所有整数数对的数位不同之和为 0 。

 

提示：

2 <= nums.length <= 105
1 <= nums[i] < 109
nums 中的整数都有相同的数位长度。
"""
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        def get_result(i):
            res = M * (M - 1) // 2
            for ii, jj in c[i].items():
                if jj == 1:
                    continue
                res -= jj * (jj - 1) // 2
            return res
        N = len(str(nums[0]))
        M = len(nums)
        c = [defaultdict(int) for _ in range(N)]
        ans = 0
        for ii in nums:
            for k, jj in enumerate(str(ii)):
                c[k][jj] += 1
        # print(c)
        for ii in range(N):
            ans += get_result(ii)
        return ans
        
            