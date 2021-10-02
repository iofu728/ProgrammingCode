# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-03 00:23:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-03 00:24:07

"""
5872. 连接后等于目标字符串的字符串对 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个 数字 字符串数组 nums 和一个 数字 字符串 target ，请你返回 nums[i] + nums[j] （两个字符串连接）结果等于 target 的下标 (i, j) （需满足 i != j）的数目。

 

示例 1：

输入：nums = ["777","7","77","77"], target = "7777"
输出：4
解释：符合要求的下标对包括：
- (0, 1)："777" + "7"
- (1, 0)："7" + "777"
- (2, 3)："77" + "77"
- (3, 2)："77" + "77"
示例 2：

输入：nums = ["123","4","12","34"], target = "1234"
输出：2
解释：符合要求的下标对包括
- (0, 1)："123" + "4"
- (2, 3)："12" + "34"
示例 3：

输入：nums = ["1","1","1"], target = "11"
输出：6
解释：符合要求的下标对包括
- (0, 1)："1" + "1"
- (1, 0)："1" + "1"
- (0, 2)："1" + "1"
- (2, 0)："1" + "1"
- (1, 2)："1" + "1"
- (2, 1)："1" + "1"
 

提示：

2 <= nums.length <= 100
1 <= nums[i].length <= 100
2 <= target.length <= 100
nums[i] 和 target 只包含数字。
nums[i] 和 target 不含有任何前导 0 。
"""
from collections import defaultdict


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        s, e = defaultdict(int), defaultdict(int)
        for ii in nums:
            if target.startswith(ii):
                s[len(ii)] += 1
            if target.endswith(ii):
                e[len(ii)] += 1
        res = 0
        for ii, jj in s.items():
            need = len(target) - ii
            if need == ii and target[:ii] == target[-ii:]:
                res += jj * (e[need] - 1)
            else:
                res += jj * e[need]
        return res