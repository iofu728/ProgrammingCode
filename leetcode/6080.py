"""
6080. 使数组按非递减顺序排列 显示英文描述 
通过的用户数0
尝试过的用户数17
用户总通过次数0
用户总提交次数18
题目难度Medium
给你一个下标从 0 开始的整数数组 nums 。在一步操作中，移除所有满足 nums[i - 1] > nums[i] 的 nums[i] ，其中 0 < i < nums.length 。

重复执行步骤，直到 nums 变为 非递减 数组，返回所需执行的操作数。

 

示例 1：

输入：nums = [5,3,4,4,7,3,6,11,8,5,11]
输出：3
解释：执行下述几个步骤：
- 步骤 1 ：[5,3,4,4,7,3,6,11,8,5,11] 变为 [5,4,4,7,6,11,11]
- 步骤 2 ：[5,4,4,7,6,11,11] 变为 [5,4,7,11,11]
- 步骤 3 ：[5,4,7,11,11] 变为 [5,7,11,11]
[5,7,11,11] 是一个非递减数组，因此，返回 3 。
示例 2：

输入：nums = [4,5,7,7,13]
输出：0
解释：nums 已经是一个非递减数组，因此，返回 0 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""


class Solution:
    def totalSteps(self, nums: List[int]) -> int:

        def get_k(nums):
            tmp, res = [nums[0]], 1
            N = len(nums)
            for ii in range(N - 1):
                ii = nums[ii + 1]
                x = bisect.bisect_right(tmp, ii)
                if x == len(tmp):
                    tmp.append(ii)
                    res = max(res, len(tmp))
                else:
                    tmp[x] = ii
            return res

        def get_num(x):
            res = 0
            t = []
            for ii, jj in enumerate(x):
                if len(t) == 0 or x[ii - 1] > jj:
                    t.append([])
                t[-1].append(jj)
            # print(t)
            while len(t) > 1:
                tmp = []
                for ii in t:
                    if len(ii) == 1:
                        continue
                    if tmp and tmp[-1][-1] <= ii[1]:
                        tmp[-1].extend(ii[1:])
                    else:
                        tmp.append(ii[1:])
                res += 1
                t = tmp
                # print(t)
            if t:
                res += len(t[0])
            return res

        res = 0
        pre = nums[0]
        idx = 1
        N = len(nums)
        while idx < N:
            b = idx
            while idx < N and nums[idx] < pre:
                idx += 1
            # print(b, idx)
            if b != idx:
                res = max(res, get_num(nums[b:idx]))
            if idx < N:
                pre = nums[idx]
            idx += 1
        return res
