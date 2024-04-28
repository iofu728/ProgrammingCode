'''
100285. 找出与数组相加的整数 I 显示英文描述
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你两个长度相等的数组 nums1 和 nums2。

数组 nums1 中的每个元素都与变量 x 所表示的整数相加。如果 x 为负数，则表现为元素值的减少。

在与 x 相加后，nums1 和 nums2 相等 。当两个数组中包含相同的整数，并且这些整数出现的频次相同时，两个数组 相等 。

返回整数 x 。



示例 1:

输入：nums1 = [2,6,4], nums2 = [9,7,5]

输出：3

解释：

与 3 相加后，nums1 和 nums2 相等。

示例 2:

输入：nums1 = [10], nums2 = [5]

输出：-5

解释：

与 -5 相加后，nums1 和 nums2 相等。

示例 3:

输入：nums1 = [1,1,1,1], nums2 = [1,1,1,1]

输出：0

解释：

与 0 相加后，nums1 和 nums2 相等。



提示：

1 <= nums1.length == nums2.length <= 100
0 <= nums1[i], nums2[i] <= 1000
测试用例以这样的方式生成：存在一个整数 x，使得 nums1 中的每个元素都与 x 相加后，nums1 与 nums2 相等。
'''

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        return nums2[0] - nums1[0]
