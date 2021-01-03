# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-01-03 11:03:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-01-03 11:23:04

'''
5643. 将数组分成三个子数组的方案数 显示英文描述 
通过的用户数60
尝试过的用户数158
用户总通过次数60
用户总提交次数281
题目难度Medium
我们称一个分割整数数组的方案是 好的 ，当它满足：

数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。
left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。
给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 109 + 7 取余后返回。

 

示例 1：

输入：nums = [1,1,1]
输出：1
解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。
示例 2：

输入：nums = [1,2,2,2,5,0]
输出：3
解释：nums 总共有 3 种好的分割方案：
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
示例 3：

输入：nums = [3,2,1]
输出：0
解释：没有好的分割方案。
 

提示：

3 <= nums.length <= 105
0 <= nums[i] <= 104
'''
import bisect
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        N = len(nums)
        sums = [nums[0]]
        for ii in range(1, N):
            sums.append(sums[-1] +  nums[ii])
        res = 0
        for left in range(N - 2):
            L = sums[left]
            mb = bisect.bisect_left(sums, 2 * L)
            if mb == N:
                break
            mb = min(max(left + 1, mb), N - 1)
            me = bisect.bisect_right(sums, (sums[-1] + L) // 2)
            me  = min(max(left + 1, me), N - 1)
            # print(L, mb, me, (sums[-1] + L) // 2)
            if me >= mb:
                res += (me - mb)
                res %= (10 ** 9 + 7)
        return res
            
        
        