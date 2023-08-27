# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-27 14:21:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-27 14:21:46

"""
8021. 使子序列的和等于目标的最少操作次数 显示英文描述 
通过的用户数731
尝试过的用户数1491
用户总通过次数758
用户总提交次数3946
题目难度Medium
给你一个下标从 0 开始的数组 nums ，它包含 非负 整数，且全部为 2 的幂，同时给你一个整数 target 。

一次操作中，你必须对数组做以下修改：

选择数组中一个元素 nums[i] ，满足 nums[i] > 1 。
将 nums[i] 从数组中删除。
在 nums 的 末尾 添加 两个 数，值都为 nums[i] / 2 。
你的目标是让 nums 的一个 子序列 的元素和等于 target ，请你返回达成这一目标的 最少操作次数 。如果无法得到这样的子序列，请你返回 -1 。

数组中一个 子序列 是通过删除原数组中一些元素，并且不改变剩余元素顺序得到的剩余数组。

 

示例 1：

输入：nums = [1,2,8], target = 7
输出：1
解释：第一次操作中，我们选择元素 nums[2] 。数组变为 nums = [1,2,4,4] 。
这时候，nums 包含子序列 [1,2,4] ，和为 7 。
无法通过更少的操作得到和为 7 的子序列。
示例 2：

输入：nums = [1,32,1,2], target = 12
输出：2
解释：第一次操作中，我们选择元素 nums[1] 。数组变为 nums = [1,1,2,16,16] 。
第二次操作中，我们选择元素 nums[3] 。数组变为 nums = [1,1,2,16,8,8] 。
这时候，nums 包含子序列 [1,1,2,8] ，和为 12 。
无法通过更少的操作得到和为 12 的子序列。
示例 3：

输入：nums = [1,32,1], target = 35
输出：-1
解释：无法得到和为 35 的子序列。
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 230
nums 只包含非负整数，且均为 2 的幂。
1 <= target < 231
"""
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        c = [0] * 31
        for ii in nums:
            k = int(math.log(ii, 2))
            c[k] += 1
        # print(c)
        y = bin(target)[2::][::-1]
        target = [int(ii) for ii in y]
        up = [ii for ii in c]
        flag = False
        for ii in range(len(target) - 1):
            # print(ii, target[ii], up[ii], flag)
            if target[ii] == 1 or flag:
                keep = int(flag) + int(target[ii] == 1)
                if up[ii] >= keep:
                    up[ii + 1] += (up[ii] - keep) // 2
                    up[ii] = keep + (up[ii] - keep) % 2
                    flag = False
            else:
                up[ii + 1] += up[ii] // 2
                up[ii] = up[ii] % 2
            if target[ii] == 1 and up[ii] == 0:
                flag = True
        # print(up)
        for ii in range(len(y)):
            if target[ii] == 1 and up[ii] >= 1:
                target[ii] -= 1
                up[ii] -= 1
        while len(target) and target[-1] == 0:
            target.pop()
        if all(target[ii] == 0 or (target[ii] == 1 and up[ii] == 1) for ii in range(len(target))):
            return 0
        res = 0
        idx = 0
        while idx < len(target):
            if target[idx] == 0:
                idx += 1
                continue
            y = idx + 1
            while y < len(up) and up[y] == 0:
                y += 1
            up[y] -= 1
            res += (y - idx)
            # print(y, idx)
            while idx < len(target) and idx < y:
                idx += 1
        return res
                
            
            
        