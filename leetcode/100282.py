'''
100282. 数组最后一个元素的最小值 显示英文描述
通过的用户数23
尝试过的用户数38
用户总通过次数23
用户总提交次数49
题目难度Medium
给你两个整数 n 和 x 。你需要构造一个长度为 n 的 正整数 数组 nums ，对于所有 0 <= i < n - 1 ，满足 nums[i + 1] 大于 nums[i] ，并且数组 nums 中所有元素的按位 AND 运算结果为 x 。

返回 nums[n - 1] 可能的 最小 值。



示例 1：

输入：n = 3, x = 4

输出：6

解释：

数组 nums 可以是 [4,5,6] ，最后一个元素为 6 。

示例 2：

输入：n = 2, x = 7

输出：15

解释：

数组 nums 可以是 [7,15] ，最后一个元素为 15 。



提示：

1 <= n, x <= 108
'''

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        b = list(bin(x)[2:])
        a = list(bin(n - 1)[2:])
        j = len(a) - 1
        # print(a, b)
        for i in range(len(b) - 1, -1, -1):
            if b[i] == "0":
                b[i] = a[j]
                j -= 1
                if j < 0:
                    break
        # print(a, b, j)
        if j >= 0:
            b = a[:j + 1] + b

        return int("".join(b), 2)
