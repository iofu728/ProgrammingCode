'''
100257. 找出唯一性数组的中位数 显示英文描述
通过的用户数13
尝试过的用户数30
用户总通过次数15
用户总提交次数50
题目难度Hard
给你一个整数数组 nums 。数组 nums 的 唯一性数组 是一个按元素从小到大排序的数组，包含了 nums 的所有非空子数组中不同元素的个数。

换句话说，这是由所有 0 <= i <= j < nums.length 的 distinct(nums[i..j]) 组成的递增数组。

其中，distinct(nums[i..j]) 表示从下标 i 到下标 j 的子数组中不同元素的数量。

返回 nums 唯一性数组 的 中位数 。

注意，数组的 中位数 定义为有序数组的中间元素。如果有两个中间元素，则取值较小的那个。



示例 1：

输入：nums = [1,2,3]

输出：1

解释：

nums 的唯一性数组为 [distinct(nums[0..0]), distinct(nums[1..1]), distinct(nums[2..2]), distinct(nums[0..1]), distinct(nums[1..2]), distinct(nums[0..2])]，即 [1, 1, 1, 2, 2, 3] 。唯一性数组的中位数为 1 ，因此答案是 1 。

示例 2：

输入：nums = [3,4,3,4,5]

输出：2

解释：

nums 的唯一性数组为 [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] 。唯一性数组的中位数为 2 ，因此答案是 2 。

示例 3：

输入：nums = [4,3,5,4]

输出：2

解释：

nums 的唯一性数组为 [1, 1, 1, 1, 2, 2, 2, 3, 3, 3] 。唯一性数组的中位数为 2 ，因此答案是 2 。



提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = n*(n+1)//2
        mid = (s+1)//2
        l1 = 1
        r1 = n
        while l1 < r1:
            l = (l1+r1)//2
            cs = collections.defaultdict(int)
            c1 = 0

            def add(c):
                nonlocal c1
                cs[c] += 1
                if cs[c] == 1:
                    c1 += 1
            s1 = 0
            pre = 0
            for i, c in enumerate(nums):
                add(c)
                while c1 > l:
                    cs[nums[s1]] -= 1
                    if cs[nums[s1]] == 0:
                        c1 -= 1
                    s1 += 1
                pre += i-s1+1

            if pre >= mid:
                r1 = l
            else:
                l1 = l+1

        return l1
