# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-10 13:07:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-10 13:08:15


"""
5894. 至少在两个数组中出现的值 显示英文描述 
通过的用户数3063
尝试过的用户数3147
用户总通过次数3114
用户总提交次数4627
题目难度Easy
给你三个整数数组 nums1、nums2 和 nums3 ，请你构造并返回一个 不同 数组，且由 至少 在 两个 数组中出现的所有值组成。数组中的元素可以按 任意 顺序排列。
 

示例 1：

输入：nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
输出：[3,2]
解释：至少在两个数组中出现的所有值为：
- 3 ，在全部三个数组中都出现过。
- 2 ，在数组 nums1 和 nums2 中出现过。
示例 2：

输入：nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
输出：[2,3,1]
解释：至少在两个数组中出现的所有值为：
- 2 ，在数组 nums2 和 nums3 中出现过。
- 3 ，在数组 nums1 和 nums2 中出现过。
- 1 ，在数组 nums1 和 nums3 中出现过。
示例 3：

输入：nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
输出：[]
解释：不存在至少在两个数组中出现的值。
 

提示：

1 <= nums1.length, nums2.length, nums3.length <= 100
1 <= nums1[i], nums2[j], nums3[k] <= 100
"""


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        res = set()
        for ii in nums1:
            if ii in nums2 or ii in nums3:
                res.add(ii)
        for ii in nums2:
            if ii in nums3:
                res.add(ii)
        return list(res)
