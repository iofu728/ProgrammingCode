"""
6090. 极大极小游戏 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个下标从 0 开始的整数数组 nums ，其长度是 2 的幂。

对 nums 执行下述算法：

设 n 等于 nums 的长度，如果 n == 1 ，终止 算法过程。否则，创建 一个新的整数数组 newNums ，新数组长度为 n / 2 ，下标从 0 开始。
对于满足 0 <= i < n / 2 的每个 偶数 下标 i ，将 newNums[i] 赋值 为 min(nums[2 * i], nums[2 * i + 1]) 。
对于满足 0 <= i < n / 2 的每个 奇数 下标 i ，将 newNums[i] 赋值 为 max(nums[2 * i], nums[2 * i + 1]) 。
用 newNums 替换 nums 。
从步骤 1 开始 重复 整个过程。
执行算法后，返回 nums 中剩下的那个数字。

 

示例 1：



输入：nums = [1,3,5,2,4,8,2,2]
输出：1
解释：重复执行算法会得到下述数组。
第一轮：nums = [1,5,4,2]
第二轮：nums = [1,4]
第三轮：nums = [1]
1 是最后剩下的那个数字，返回 1 。
示例 2：

输入：nums = [3]
输出：3
解释：3 就是最后剩下的数字，返回 3 。
 

提示：

1 <= nums.length <= 1024
1 <= nums[i] <= 109
nums.length 是 2 的幂
"""
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [min(nums[2 * ii], nums[2 * ii + 1]) if ii % 2 == 0 else max(nums[2 * ii], nums[2 * ii + 1]) for ii in range(len(nums) // 2)]
        return nums[0]
            