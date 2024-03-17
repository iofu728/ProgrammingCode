# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-03-17 12:29:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-03-17 12:29:32

"""
100227. 拾起 K 个 1 需要的最少行动次数 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数2
题目难度Hard
给你一个下标从 0 开始的二进制数组 nums，其长度为 n ；另给你一个 正整数 k 以及一个 非负整数 maxChanges 。

灵茶山艾府在玩一个游戏，游戏的目标是让灵茶山艾府使用 最少 数量的 行动 次数从 nums 中拾起 k 个 1 。游戏开始时，灵茶山艾府可以选择数组 [0, n - 1] 范围内的任何索引index 站立。如果 nums[index] == 1 ，灵茶山艾府就会拾起一个 1 ，并且 nums[index] 变成0（这 不算 作一次行动）。之后，灵茶山艾府可以执行 任意数量 的 行动（包括零次），在每次行动中灵茶山艾府必须 恰好 执行以下动作之一：

选择任意一个下标 j != index 且满足 nums[j] == 0 ，然后将 nums[j] 设置为 1 。这个动作最多可以执行 maxChanges 次。
选择任意两个相邻的下标 x 和 y（|x - y| == 1）且满足 nums[x] == 1, nums[y] == 0 ，然后交换它们的值（将 nums[y] = 1 和 nums[x] = 0）。如果 y == index，在这次行动后灵茶山艾府拾起一个 1 ，并且 nums[y] 变成 0 。
返回灵茶山艾府拾起 恰好 k 个 1 所需的 最少 行动次数。

 

示例 1：

输入：nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1

输出：3

解释：如果游戏开始时灵茶山艾府在 index == 1 的位置上，按照以下步骤执行每个动作，他可以利用 3 次行动拾取 3 个 1 ：

游戏开始时灵茶山艾府拾取了一个 1 ，nums[1] 变成了 0。此时 nums 变为 [1,0,0,0,0,1,1,0,0,1] 。
选择 j == 2 并执行第一种类型的动作。nums 变为 [1,0,1,0,0,1,1,0,0,1]
选择 x == 2 和 y == 1 ，并执行第二种类型的动作。nums 变为 [1,1,0,0,0,1,1,0,0,1] 。由于 y == index，灵茶山艾府拾取了一个 1 ，nums 变为  [1,0,0,0,0,1,1,0,0,1] 。
选择 x == 0 和 y == 1 ，并执行第二种类型的动作。nums 变为 [0,1,0,0,0,1,1,0,0,1] 。由于 y == index，灵茶山艾府拾取了一个 1 ，nums 变为  [0,0,0,0,0,1,1,0,0,1] 。
请注意，灵茶山艾府也可能执行其他的 3 次行动序列达成拾取 3 个 1 。

示例 2：

输入：nums = [0,0,0,0], k = 2, maxChanges = 3

输出：4

解释：如果游戏开始时灵茶山艾府在 index == 0 的位置上，按照以下步骤执行每个动作，他可以利用 4 次行动拾取 2 个 1 ：

选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。
选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于 y == index，灵茶山艾府拾起了一个 1 ，nums 变为 [0,0,0,0] 。
再次选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。
再次选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于y == index，灵茶山艾府拾起了一个 1 ，nums 变为 [0,0,0,0] 。
 

提示：

2 <= n <= 105
0 <= nums[i] <= 1
1 <= k <= 105
0 <= maxChanges <= 105
maxChanges + sum(nums) >= k
"""
class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        n = len(nums)
        if sum(nums) == 0 :
            return 2 * k
        if k == 1 :
            return 0
        
        mark2 = mark3 = False
        for i in range(n-1) :
            if nums[i] == nums[i+1] == 1 :
                mark2 = True
                break
        for i in range(n-2) :
            if nums[i] == nums[i+1] == nums[i+2] == 1:
                mark3 = True
                break
    
        # print(mark2, mark3)
        if mark3 :
            if k <= 3 :
                return k-1
            elif k - maxChanges <= 3 :
                return 2 + 2 * (k-3)
        elif mark2 :
            if k <= 2 :
                return k-1
            elif k - maxChanges <= 2 :
                return 1 + 2 * (k-2)
        if k - maxChanges <= 1 :
            return 2 * (k-1)
        k -= maxChanges 
        to_ret_base = 2 * maxChanges
        idx = [i for i, t in enumerate(nums) if t == 1]
        # print(k, idx, to_ret_base)
        
        presum = [0]
        for t in idx :
            presum.append(presum[-1]+t)
        to_ret = 1e99
        for s in range(0, len(idx)-k+1) :
            e = s + k - 1
            mid = (s+e)//2
            # print(s, mid, e)
            small_part = idx[mid]*(mid-s) - (presum[mid]-presum[s])
            large_part = -idx[mid]*(e-mid) + (presum[e+1]-presum[mid+1])
            to_ret = min(to_ret, small_part+large_part)
            
        return to_ret + to_ret_base