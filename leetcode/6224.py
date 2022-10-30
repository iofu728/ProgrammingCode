# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-23 11:26:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-23 11:26:31

"""
6224. 最大公因数等于 K 的子数组数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的子数组中元素的最大公因数等于 k 的子数组数目。

子数组 是数组中一个连续的非空序列。

数组的最大公因数 是能整除数组中所有元素的最大整数。

 

示例 1：

输入：nums = [9,3,1,2,6,3], k = 3
输出：4
解释：nums 的子数组中，以 3 作为最大公因数的子数组如下：
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
示例 2：

输入：nums = [4], k = 7
输出：0
解释：不存在以 7 作为最大公因数的子数组。
 

提示：

1 <= nums.length <= 1000
1 <= nums[i], k <= 109
"""
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ka = []
        nums = [ii // k if ii % k == 0 else 0 for ii in nums]
        for ii, jj in enumerate(nums):
            if jj == 0:
                continue
            if len(ka) == 0 or ka[-1][-1] != ii - 1:
                ka.append([])
            ka[-1].append(ii)
        res = 0
        # print(nums, ka)
        for ii in ka:
            for l in range(ii[0], ii[-1] + 1):
                tmp = nums[l]
                if tmp == 1:
                    # print(ii)
                    res += (ii[-1] + 1 - l)
                    continue
                for r in range(l + 1, ii[-1] + 1):
                    tmp = math.gcd(tmp, nums[r])
                    if tmp == 1:
                        # print(ii, r)
                        res += (ii[-1] + 1 - r)
                        break
        return res
            
        