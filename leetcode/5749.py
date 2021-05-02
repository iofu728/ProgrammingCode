# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-05-02 12:07:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-05-02 12:07:21

"""
5749. 邻位交换的最小次数 显示英文描述 
通过的用户数4
尝试过的用户数9
用户总通过次数4
用户总提交次数9
题目难度Medium
给你一个表示大整数的字符串 num ，和一个整数 k 。

如果某个整数是 num 中各位数字的一个 排列 且它的 值大于 num ，则称这个整数为 妙数 。可能存在很多妙数，但是只需要关注 值最小 的那些。

例如，num = "5489355142" ：
第 1 个最小妙数是 "5489355214"
第 2 个最小妙数是 "5489355241"
第 3 个最小妙数是 "5489355412"
第 4 个最小妙数是 "5489355421"
返回要得到第 k 个 最小妙数 需要对 num 执行的 相邻位数字交换的最小次数 。

测试用例是按存在第 k 个最小妙数而生成的。

 

示例 1：

输入：num = "5489355142", k = 4
输出：2
解释：第 4 个最小妙数是 "5489355421" ，要想得到这个数字：
- 交换下标 7 和下标 8 对应的位："5489355142" -> "5489355412"
- 交换下标 8 和下标 9 对应的位："5489355412" -> "5489355421"
示例 2：

输入：num = "11112", k = 4
输出：4
解释：第 4 个最小妙数是 "21111" ，要想得到这个数字：
- 交换下标 3 和下标 4 对应的位："11112" -> "11121"
- 交换下标 2 和下标 3 对应的位："11121" -> "11211"
- 交换下标 1 和下标 2 对应的位："11211" -> "12111"
- 交换下标 0 和下标 1 对应的位："12111" -> "21111"
示例 3：

输入：num = "00123", k = 1
输出：1
解释：第 1 个最小妙数是 "00132" ，要想得到这个数字：
- 交换下标 3 和下标 4 对应的位："00123" -> "00132"
 

提示：

2 <= num.length <= 1000
1 <= k <= 1000
num 仅由数字组成
"""


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def nextPermutation(nums: List[int]) -> None:
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            if i >= 0:
                j = len(nums) - 1
                while j >= 0 and nums[i] >= nums[j]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]

            left, right = i + 1, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        nums = [int(ii) for ii in num]
        for _ in range(k):
            nextPermutation(nums)
        # print(nums)
        res = 0
        for ii in range(len(nums)):
            t = int(num[ii])
            idx = nums.index(t)
            res += idx
            nums.pop(idx)
            # print(idx, nums)
        return res
