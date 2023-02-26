# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-02-26 12:06:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-02-26 12:06:37

"""
6367. 求出最多标记下标 显示英文描述 
通过的用户数4
尝试过的用户数14
用户总通过次数4
用户总提交次数15
题目难度Medium
给你一个下标从 0 开始的整数数组 nums 。

一开始，所有下标都没有被标记。你可以执行以下操作任意次：

选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。

 

示例 1：

输入：nums = [3,5,2,4]
输出：2
解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
没有其他更多可执行的操作，所以答案为 2 。
示例 2：

输入：nums = [9,2,5,4]
输出：4
解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
没有其他更多可执行的操作，所以答案为 4 。
示例 3：

输入：nums = [7,6,8]
输出：0
解释：没有任何可以执行的操作，所以答案为 0 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        N = len(nums)
        nums = sorted(nums)
        l, r = 0, N // 2
        res = 0
        done = set()
        
        # for r, x in enumerate(nums):
        #     if r in done:
        #         continue
        #     l1 = bisect.bisect_left(nums, -((-x) // 2), l)
        #     print(r, x, l1)
        #     if l1 < N:
        #         res += 2
        #         done.add(l1)
        #     else:
        #         break
        #     l = l1 + 1
        for l, x in enumerate(nums):
            if l in done:
                continue
            r1 = bisect.bisect_left(nums, 2 * x, r)
            # print(l, x, r1)
            if r1 < N:
                res += 2
                done.add(r1)
            else:
                break
            r = r1 + 1
            
        return res
        