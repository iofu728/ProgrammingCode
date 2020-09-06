# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-06 10:44:16
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 10:59:47

"""
5508. 数的平方等于两数乘积的方法数 显示英文描述 
通过的用户数131
尝试过的用户数204
用户总通过次数131
用户总提交次数268
题目难度Medium
给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：

类型 1：三元组 (i, j, k) ，如果 nums1[i]2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.length 且 0 <= j < k < nums2.length
类型 2：三元组 (i, j, k) ，如果 nums2[i]2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.length 且 0 <= j < k < nums1.length
 

示例 1：

输入：nums1 = [7,4], nums2 = [5,2,8,9]
输出：1
解释：类型 1：(1,1,2), nums1[1]^2 = nums2[1] * nums2[2] (4^2 = 2 * 8)
示例 2：

输入：nums1 = [1,1], nums2 = [1,1,1]
输出：9
解释：所有三元组都符合题目要求，因为 1^2 = 1 * 1
类型 1：(0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2), nums1[i]^2 = nums2[j] * nums2[k]
类型 2：(0,0,1), (1,0,1), (2,0,1), nums2[i]^2 = nums1[j] * nums1[k]
示例 3：

输入：nums1 = [7,7,8,3], nums2 = [1,2,9,7]
输出：2
解释：有两个符合题目要求的三元组
类型 1：(3,0,2), nums1[3]^2 = nums2[0] * nums2[2]
类型 2：(3,0,1), nums2[3]^2 = nums1[0] * nums1[1]
示例 4：

输入：nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
输出：0
解释：不存在符合题目要求的三元组
 

提示：

1 <= nums1.length, nums2.length <= 1000
1 <= nums1[i], nums2[i] <= 10^5
"""
from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        a_map, b_map = defaultdict(int), defaultdict(int)
        res = 0
        for ii, jj in enumerate(nums1):
            a_map[jj] += 1
        for ii, jj in enumerate(nums2):
            b_map[jj] += 1
        for n1, s1 in a_map.items():
            for n2, s2 in b_map.items():
                t1, t2 = (n1 ** 2) % n2, (n1 ** 2) // n2
                t3, t4 = (n2 ** 2) % n1, (n2 ** 2) // n1
                if not t1 and t2 in b_map and t2 >= n2:
                    if n2 == t2:
                        # print("==1", n1, n2, s1, s2)
                        res += s1 * s2 * (s2 - 1) // 2
                    else:
                        # print("!=1", n1, n2, t2, s1, s2, b_map[t2])
                        res += s1 * s2 * b_map[t2]
                if not t3 and t4 in a_map and t4 >= n1:
                    if n1 == t4:
                        # print("==2", n1, n2, s1, s2)
                        res += s2 * s1 * (s1 - 1) // 2
                    else:
                        # print("!=2", n1, n2, t4, s1, s2, b_map[t4])
                        res += s2 * s1 * a_map[t4]
        return res

