# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-04-09 12:11:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-04-09 12:11:12

"""
6360. 等值距离和 显示英文描述 
通过的用户数0
尝试过的用户数6
用户总通过次数0
用户总提交次数6
题目难度Medium
给你一个下标从 0 开始的整数数组 nums 。现有一个长度等于 nums.length 的数组 arr 。对于满足 nums[j] == nums[i] 且 j != i 的所有 j ，arr[i] 等于所有 |i - j| 之和。如果不存在这样的 j ，则令 arr[i] 等于 0 。

返回数组 arr 。

 

示例 1：

输入：nums = [1,3,1,1,2]
输出：[5,0,3,4,0]
解释：
i = 0 ，nums[0] == nums[2] 且 nums[0] == nums[3] 。因此，arr[0] = |0 - 2| + |0 - 3| = 5 。 
i = 1 ，arr[1] = 0 因为不存在值等于 3 的其他下标。
i = 2 ，nums[2] == nums[0] 且 nums[2] == nums[3] 。因此，arr[2] = |2 - 0| + |2 - 3| = 3 。
i = 3 ，nums[3] == nums[0] 且 nums[3] == nums[2] 。因此，arr[3] = |3 - 0| + |3 - 2| = 4 。 
i = 4 ，arr[4] = 0 因为不存在值等于 2 的其他下标。
示例 2：

输入：nums = [0,5,3]
输出：[0,0,0]
解释：因为 nums 中的元素互不相同，对于所有 i ，都有 arr[i] = 0 。
 

提示：

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        c = defaultdict(list)
        for ii, jj in enumerate(nums):
            c[jj].append(ii)
        res = [0] * len(nums)
        for k, v in c.items():
            if len(v) == 1:
                continue
            idx = 0
            s = sum(i - v[0] for i in v[1:])
            res[v[0]] = s
            a, b = 1, len(v) - 1
            # print(s, v)
            for idx in range(1, len(v)):
                g = v[idx] - v[idx - 1]
                s = s + a * g - b * g
                a += 1
                b -= 1
                res[v[idx]] = s
        return res
                