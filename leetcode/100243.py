# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-03-03 13:30:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-03-03 13:31:07

"""
100243. 将元素分配到两个数组中 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个下标从 1 开始、包含 不同 整数的数组 nums ，数组长度为 n 。

你需要通过 n 次操作，将 nums 中的所有元素分配到两个数组 arr1 和 arr2 中。在第一次操作中，将 nums[1] 追加到 arr1 。在第二次操作中，将 nums[2] 追加到 arr2 。之后，在第 i 次操作中：

如果 arr1 的最后一个元素 大于 arr2 的最后一个元素，就将 nums[i] 追加到 arr1 。否则，将 nums[i] 追加到 arr2 。
通过连接数组 arr1 和 arr2 形成数组 result 。例如，如果 arr1 == [1,2,3] 且 arr2 == [4,5,6] ，那么 result = [1,2,3,4,5,6] 。

返回数组 result 。

 

示例 1：

输入：nums = [2,1,3]
输出：[2,3,1]
解释：在前两次操作后，arr1 = [2] ，arr2 = [1] 。
在第 3 次操作中，由于 arr1 的最后一个元素大于 arr2 的最后一个元素（2 > 1），将 nums[3] 追加到 arr1 。
3 次操作后，arr1 = [2,3] ，arr2 = [1] 。
因此，连接形成的数组 result 是 [2,3,1] 。
示例 2：

输入：nums = [5,4,3,8]
输出：[5,3,4,8]
解释：在前两次操作后，arr1 = [5] ，arr2 = [4] 。
在第 3 次操作中，由于 arr1 的最后一个元素大于 arr2 的最后一个元素（5 > 4），将 nums[3] 追加到 arr1 ，因此 arr1 变为 [5,3] 。
在第 4 次操作中，由于 arr2 的最后一个元素大于 arr1 的最后一个元素（4 > 3），将 nums[4] 追加到 arr2 ，因此 arr2 变为 [4,8] 。
4 次操作后，arr1 = [5,3] ，arr2 = [4,8] 。
因此，连接形成的数组 result 是 [5,3,4,8] 。
 

提示：

3 <= n <= 50
1 <= nums[i] <= 100
nums中的所有元素都互不相同。
"""
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a, b = [nums[0]], [nums[1]]
        N = len(nums)
        for ii in range(2, N):
            if a[-1] > b[-1]:
                a.append(nums[ii])
            else:
                b.append(nums[ii])
        return a + b