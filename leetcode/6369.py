# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-02-26 12:05:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-02-26 12:05:53

"""
6369. 左右元素和的差值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个下标从 0 开始的整数数组 nums ，请你找出一个下标从 0 开始的整数数组 answer ，其中：

answer.length == nums.length
answer[i] = |leftSum[i] - rightSum[i]|
其中：

leftSum[i] 是数组 nums 中下标 i 左侧元素之和。如果不存在对应的元素，leftSum[i] = 0 。
rightSum[i] 是数组 nums 中下标 i 右侧元素之和。如果不存在对应的元素，rightSum[i] = 0 。
返回数组 answer 。

 

示例 1：

输入：nums = [10,4,8,3]
输出：[15,1,11,22]
解释：数组 leftSum 为 [0,10,14,22] 且数组 rightSum 为 [15,11,3,0] 。
数组 answer 为 [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22] 。
示例 2：

输入：nums = [1]
输出：[0]
解释：数组 leftSum 为 [0] 且数组 rightSum 为 [0] 。
数组 answer 为 [|0 - 0|] = [0] 。
 

提示：

1 <= nums.length <= 1000
"""
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        s = [0]
        for ii in nums:
            s.append(s[-1] + ii)
        ss = [0] * len(nums)
        for ii in range(len(nums) - 2, -1, -1):
            ss[ii] = ss[ii + 1] + nums[ii + 1]
        # print(s, ss)
        return [abs(ii - jj) for ii, jj in zip(s, ss)]
            
            

        # return [abs(get_left(ii) - get_right(ii)) for ii, jj in enumerate(nums)]