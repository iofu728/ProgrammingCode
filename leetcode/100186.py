# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-02-11 11:07:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-02-11 11:08:01

"""
100186. 匹配模式数组的子数组数目 I 显示英文描述 
通过的用户数12
尝试过的用户数16
用户总通过次数12
用户总提交次数17
题目难度Medium
给你一个下标从 0 开始长度为 n 的整数数组 nums ，和一个下标从 0 开始长度为 m 的整数数组 pattern ，pattern 数组只包含整数 -1 ，0 和 1 。

大小为 m + 1 的子数组 nums[i..j] 如果对于每个元素 pattern[k] 都满足以下条件，那么我们说这个子数组匹配模式数组 pattern ：

如果 pattern[k] == 1 ，那么 nums[i + k + 1] > nums[i + k]
如果 pattern[k] == 0 ，那么 nums[i + k + 1] == nums[i + k]
如果 pattern[k] == -1 ，那么 nums[i + k + 1] < nums[i + k]
请你返回匹配 pattern 的 nums 子数组的 数目 。

 

示例 1：

输入：nums = [1,2,3,4,5,6], pattern = [1,1]
输出：4
解释：模式 [1,1] 说明我们要找的子数组是长度为 3 且严格上升的。在数组 nums 中，子数组 [1,2,3] ，[2,3,4] ，[3,4,5] 和 [4,5,6] 都匹配这个模式。
所以 nums 中总共有 4 个子数组匹配这个模式。
示例 2：

输入：nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]
输出：2
解释：这里，模式数组 [1,0,-1] 说明我们需要找的子数组中，第一个元素小于第二个元素，第二个元素等于第三个元素，第三个元素大于第四个元素。在 nums 中，子数组 [1,4,4,1] 和 [3,5,5,3] 都匹配这个模式。
所以 nums 中总共有 2 个子数组匹配这个模式。
 

提示：

2 <= n == nums.length <= 100
1 <= nums[i] <= 109
1 <= m == pattern.length < n
-1 <= pattern[i] <= 1
"""
def compute_lps_array(pattern):
    """
    计算给定数组的最长公共前后缀（LPS）数组。
    """
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    KMP搜索算法，用于在text数组中查找pattern数组的所有出现。
    返回pattern在text中出现的次数。
    """
    lps = compute_lps_array(pattern)
    i = 0  # index for text[]
    j = 0  # index for pattern[]
    matches = 0

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            matches += 1  # 找到一个匹配
            j = lps[j-1]

        # 匹配失败后，移动模式串的指针
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return matches

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_v(x, y):
            if nums[x] == nums[y]:
                return 0
            return -1 if nums[x] > nums[y] else 1
        N = len(nums)
        p = [get_v(ii - 1, ii) for ii in range(1, N)]
        return kmp_search(p, pattern)
