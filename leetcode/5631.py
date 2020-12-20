import heapq
'''
5631. 跳跃游戏 VI 显示英文描述 
通过的用户数114
尝试过的用户数241
用户总通过次数114
用户总提交次数289
题目难度Medium
给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。

一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。

你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。

请你返回你能得到的 最大得分 。

 

示例 1：

输入：nums = [1,-1,-2,4,-7,3], k = 2
输出：7
解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。
示例 2：

输入：nums = [10,-5,-2,4,0,3], k = 3
输出：17
解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。
示例 3：

输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
输出：0
 

提示：

 1 <= nums.length, k <= 105
-104 <= nums[i] <= 104
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = []
        heapq.heappush(dp, (0, 0))
        tmp_max = 0
        for ii in range(1, N):
            t, idx = heapq.heappop(dp)
            while idx + k <  ii:
                t, idx = heapq.heappop(dp)
            # print(dp,  t, idx)
            tmp_max = t * -1 + nums[ii]
            heapq.heappush(dp, (tmp_max *  -1, ii))
            heapq.heappush(dp, (t, idx))
        return tmp_max + nums[0]
                
                