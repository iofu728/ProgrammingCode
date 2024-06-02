# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-02 12:03:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-02 12:03:15

"""
100315. 找到按位与最接近 K 的子数组 显示英文描述 
通过的用户数28
尝试过的用户数37
用户总通过次数28
用户总提交次数44
题目难度Hard
给你一个数组 nums 和一个整数 k 。你需要找到 nums 的一个 子数组 ，满足子数组中所有元素按位与运算 AND 的值与 k 的 绝对差 尽可能 小 。换言之，你需要选择一个子数组 nums[l..r] 满足 |k - (nums[l] AND nums[l + 1] ... AND nums[r])| 最小。

请你返回 最小 的绝对差值。

子数组是数组中连续的 非空 元素序列。

 

示例 1：

输入：nums = [1,2,4,5], k = 3

输出：1

解释：

子数组 nums[2..3] 的按位 AND 运算值为 4 ，得到最小差值 |3 - 4| = 1 。

示例 2：

输入：nums = [1,2,1,2], k = 2

输出：0

解释：

子数组 nums[1..1] 的按位 AND 运算值为 2 ，得到最小差值 |2 - 2| = 0 。

示例 3：

输入：nums = [1], k = 10

输出：9

解释：

只有一个子数组，按位 AND 运算值为 1 ，得到最小差值 |10 - 1| = 9 。

 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        a = []
        ans = None
        for x in nums:
            a.append(x)
            b = []
            for ai in a:
                ai = ai & x
                if len(b) and b[-1] == ai:
                    continue
                b.append(ai)
            a = b
            for ai in a:
                d = abs(ai - k)
                if ans is None or ans > d:
                    ans = d
        return ans
                
                