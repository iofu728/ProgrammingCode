# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-10-29 11:44:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-10-29 11:44:27

"""
100111. 找出数组中的 K-or 值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。

nums 中的 K-or 是一个满足以下条件的非负整数：

只有在 nums 中，至少存在 k 个元素的第 i 位值为 1 ，那么 K-or 中的第 i 位的值才是 1 。
返回 nums 的 K-or 值。

注意 ：对于整数 x ，如果 (2i AND x) == 2i ，则 x 中的第 i 位值为 1 ，其中 AND 为按位与运算符。

 

示例 1：

输入：nums = [7,12,9,8,9,15], k = 4
输出：9
解释：nums[0]、nums[2]、nums[4] 和 nums[5] 的第 0 位的值为 1 。
nums[0] 和 nums[5] 的第 1 位的值为 1 。
nums[0]、nums[1] 和 nums[5] 的第 2 位的值为 1 。
nums[1]、nums[2]、nums[3]、nums[4] 和 nums[5] 的第 3 位的值为 1 。
只有第 0 位和第 3 位满足数组中至少存在 k 个元素在对应位上的值为 1 。因此，答案为 2^0 + 2^3 = 9 。
示例 2：

输入：nums = [2,12,1,11,4,5], k = 6
输出：0
解释：因为 k == 6 == nums.length ，所以数组的 6-or 等于其中所有元素按位与运算的结果。因此，答案为 2 AND 12 AND 1 AND 11 AND 4 AND 5 = 0 。
示例 3：

输入：nums = [10,8,5,9,11,6,8], k = 1
输出：15
解释：因为 k == 1 ，数组的 1-or 等于其中所有元素按位或运算的结果。因此，答案为 10 OR 8 OR 5 OR 9 OR 11 OR 6 OR 8 = 15 。
 

提示：

1 <= nums.length <= 50
0 <= nums[i] < 231
1 <= k <= nums.length
"""
class Solution:
    def findKOr(self, nums: List[int], kk: int) -> int:
        c = defaultdict(int)
        for ii in nums:
            for j, k in enumerate(bin(ii)[2:][::-1]):
                if k == "1":
                    c[j] += 1
        res = 0
        for i in range(32):
            if c[i] >= kk:
                res += pow(2, i)
        return res