"""
3583. 统计特殊三元组
已解答
中等
premium lock icon
相关企业
提示
给你一个整数数组 nums。

特殊三元组 定义为满足以下条件的下标三元组 (i, j, k)：

0 <= i < j < k < n，其中 n = nums.length
nums[i] == nums[j] * 2
nums[k] == nums[j] * 2
返回数组中 特殊三元组 的总数。

由于答案可能非常大，请返回结果对 109 + 7 取余数后的值。

 

示例 1：

输入： nums = [6,3,6]

输出： 1

解释：

唯一的特殊三元组是 (i, j, k) = (0, 1, 2)，其中：

nums[0] = 6, nums[1] = 3, nums[2] = 6
nums[0] = nums[1] * 2 = 3 * 2 = 6
nums[2] = nums[1] * 2 = 3 * 2 = 6
示例 2：

输入： nums = [0,1,0,0]

输出： 1

解释：

唯一的特殊三元组是 (i, j, k) = (0, 2, 3)，其中：

nums[0] = 0, nums[2] = 0, nums[3] = 0
nums[0] = nums[2] * 2 = 0 * 2 = 0
nums[3] = nums[2] * 2 = 0 * 2 = 0
示例 3：

输入： nums = [8,4,2,8,4]

输出： 2

解释：

共有两个特殊三元组：

(i, j, k) = (0, 1, 3)
nums[0] = 8, nums[1] = 4, nums[3] = 8
nums[0] = nums[1] * 2 = 4 * 2 = 8
nums[3] = nums[1] * 2 = 4 * 2 = 8
(i, j, k) = (1, 2, 4)
nums[1] = 4, nums[2] = 2, nums[4] = 4
nums[1] = nums[2] * 2 = 2 * 2 = 4
nums[4] = nums[2] * 2 = 2 * 2 = 4
 

提示：

3 <= n == nums.length <= 105
0 <= nums[i] <= 105
"""
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        c1, c2 = Counter(), Counter(nums)
        n = len(nums)
        c2[nums[0]] -= 1
        res = 0
        for i in range(1, n - 1):
            b = nums[i]
            c1[nums[i - 1]] += 1
            c2[nums[i]] -= 1
            a = c1[b * 2]
            c = c2[b * 2]
            res = (res + a * c) % (10 ** 9 +7)
        return res
            
        