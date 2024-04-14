# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-04-14 13:02:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-04-14 13:02:35

"""
100265. 素数的最大距离 显示英文描述 
通过的用户数12
尝试过的用户数17
用户总通过次数12
用户总提交次数18
题目难度Medium
给你一个整数数组 nums。

返回两个（不一定不同的）素数在 nums 中 下标 的 最大距离。

 

示例 1：

输入： nums = [4,2,9,5,3]

输出： 3

解释： nums[1]、nums[3] 和 nums[4] 是素数。因此答案是 |4 - 1| = 3。

示例 2：

输入： nums = [4,8,2,8]

输出： 0

解释： nums[2] 是素数。因为只有一个素数，所以答案是 |2 - 2| = 0。

 

提示：

1 <= nums.length <= 3 * 105
1 <= nums[i] <= 100
输入保证 nums 中至少有一个素数。

"""
def euler_flag_prime(n):
    # 欧拉线性筛素数
    # 说明：返回小于等于 n 的所有素数
    flag = [False for _ in range(n + 1)]
    prime_numbers = set()
    for num in range(2, n + 1):
        if not flag[num]:
            prime_numbers.add(num)
        for prime in prime_numbers:
            if num * prime > n:
                break
            flag[num * prime] = True
            if num % prime == 0:  # 这句是最有意思的地方  下面解释
                break
    return prime_numbers

prime_numbers = euler_flag_prime(200)
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        a = []
        for ii, jj in enumerate(nums):
            if jj in prime_numbers:
                if len(a) > 1:
                    a.pop()
                a.append(ii)
        return a[-1] - a[0]
        
        