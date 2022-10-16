# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-16 12:24:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-16 12:25:31

"""
6205. 反转之后不同整数的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个由 正 整数组成的数组 nums 。

你必须取出数组中的每个整数，反转其中每个数位，并将反转后得到的数字添加到数组的末尾。这一操作只针对 nums 中原有的整数执行。

返回结果数组中 不同 整数的数目。

 

示例 1：

输入：nums = [1,13,10,12,31]
输出：6
解释：反转每个数字后，结果数组是 [1,13,10,12,31,1,31,1,21,13] 。
反转后得到的数字添加到数组的末尾并按斜体加粗表示。注意对于整数 10 ，反转之后会变成 01 ，即 1 。
数组中不同整数的数目为 6（数字 1、10、12、13、21 和 31）。
示例 2：

输入：nums = [2,2,2]
输出：1
解释：反转每个数字后，结果数组是 [2,2,2,2,2,2] 。
数组中不同整数的数目为 1（数字 2）。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 106
"""
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def convert(a):
            return int(str(a)[::-1])
        c = set(nums)
        for ii in set(nums):
            c.add(convert(ii))
        return len(c)