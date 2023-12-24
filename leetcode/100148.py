# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-12-24 12:09:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-12-24 12:09:26

"""
100148. 最小数字游戏 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
你有一个下标从 0 开始、长度为 偶数 的整数数组 nums ，同时还有一个空数组 arr 。Alice 和 Bob 决定玩一个游戏，游戏中每一轮 Alice 和 Bob 都会各自执行一次操作。游戏规则如下：

每一轮，Alice 先从 nums 中移除一个 最小 元素，然后 Bob 执行同样的操作。
接着，Bob 会将移除的元素添加到数组 arr 中，然后 Alice 也执行同样的操作。
游戏持续进行，直到 nums 变为空。
返回结果数组 arr 。

 

示例 1：

输入：nums = [5,4,2,3]
输出：[3,2,5,4]
解释：第一轮，Alice 先移除 2 ，然后 Bob 移除 3 。然后 Bob 先将 3 添加到 arr 中，接着 Alice 再将 2 添加到 arr 中。于是 arr = [3,2] 。
第二轮开始时，nums = [5,4] 。Alice 先移除 4 ，然后 Bob 移除 5 。接着他们都将元素添加到 arr 中，arr 变为 [3,2,5,4] 。
示例 2：

输入：nums = [2,5]
输出：[5,2]
解释：第一轮，Alice 先移除 2 ，然后 Bob 移除 5 。然后 Bob 先将 5 添加到 arr 中，接着 Alice 再将 2 添加到 arr 中。于是 arr = [5,2] 。
 

提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
nums.length % 2 == 0
"""
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        return [nums[ii + 1] if ii % 2 == 0 else nums[ii - 1] for ii in range(len(nums))]