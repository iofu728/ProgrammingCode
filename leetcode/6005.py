"""
6005. 使数组变成交替数组的最少操作数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个下标从 0 开始的数组 nums ，该数组由 n 个正整数组成。

如果满足下述条件，则数组 nums 是一个 交替数组 ：

nums[i - 2] == nums[i] ，其中 2 <= i <= n - 1 。
nums[i - 1] != nums[i] ，其中 1 <= i <= n - 1 。
在一步 操作 中，你可以选择下标 i 并将 nums[i] 更改 为 任一 正整数。

返回使数组变成交替数组的 最少操作数 。

 

示例 1：

输入：nums = [3,1,3,2,4,3]
输出：3
解释：
使数组变成交替数组的方法之一是将该数组转换为 [3,1,3,1,3,1] 。
在这种情况下，操作数为 3 。
可以证明，操作数少于 3 的情况下，无法使数组变成交替数组。
示例 2：

输入：nums = [1,2,2,2,2]
输出：2
解释：
使数组变成交替数组的方法之一是将该数组转换为 [1,2,1,2,1].
在这种情况下，操作数为 2 。
注意，数组不能转换成 [2,2,2,2,2] 。因为在这种情况下，nums[0] == nums[1]，不满足交替数组的条件。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        K = len(nums[::2])
        Q = N - K
        c1, c2 = Counter(nums[::2]), Counter(nums[1::2])
        a = sorted(c1.items(), key=lambda i: (-i[1], -i[0]))[:2]
        b = sorted(c2.items(), key=lambda i: (-i[1], -i[0]))[:2]
        if len(b) == 0:
            return 0
        res = 0
        if a[0][0] == b[0][0]:
            a1 = a[0][1]
            a2 = a[1][1] if len(a) > 1 else 0
            b1 = b[0][1]
            b2 = b[1][1] if len(b) > 1 else 0
            if a1 + b2 >= a2 + b1:
                if len(b) > 1:
                    res = K - a[0][1] + Q - b[1][1]
                else:
                    res = K - a[0][1] + Q
            else:
                if len(a) > 1:
                    res = Q - b[0][1] + K - a[1][1]
                else:
                    res = Q - b[0][1] + K
        else:
            res = K - a[0][1] + Q - b[0][1]
        # print(a, b)
        return res