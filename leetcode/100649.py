"""
100649. 数位和排序需要的最小交换次数 显示英文描述 
通过的用户数803
尝试过的用户数1076
用户总通过次数825
用户总提交次数1808
题目难度Medium
给你一个由 互不相同 的正整数组成的数组 nums，需要根据每个数字的数位和（即每一位数字相加求和）按 升序 对数组进行排序。如果两个数字的数位和相等，则较小的数字排在前面。

返回将 nums 排列为上述排序顺序所需的 最小 交换次数。

一次 交换 定义为交换数组中两个不同位置的值。

 

示例 1：

输入: nums = [37,100]

输出: 1

解释:

计算每个整数的数位和：[3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
根据数位和排序：[100, 37]。将 37 与 100 交换，得到排序后的数组。
因此，将 nums 排列为排序顺序所需的最小交换次数为 1。
示例 2：

输入: nums = [22,14,33,7]

输出: 0

解释:

计算每个整数的数位和：[2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
根据数位和排序：[22, 14, 33, 7]。数组已经是排序好的。
因此，将 nums 排列为排序顺序所需的最小交换次数为 0。
示例 3：

输入: nums = [18,43,34,16]

输出: 2

解释:

计算每个整数的数位和：[1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
根据数位和排序：[16, 34, 43, 18]。将 18 与 16 交换，再将 43 与 34 交换，得到排序后的数组。
因此，将 nums 排列为排序顺序所需的最小交换次数为 2。
 

提示:

1 <= nums.length <= 105
1 <= nums[i] <= 109
nums 由 互不相同 的正整数组成。

"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        arr = [sum(int(ii) for ii in str(i)) for i in nums]
        
        arr_pos = [(val, idx) for idx, val in enumerate(arr)]
        arr_pos = sorted(arr_pos, key=lambda i:(i[0], nums[i[1]]))
        # arr_pos.sort()
        # arr_now = [arr[i] for i, (val, idx) in enumerate(arr_pos) if arr[i] != val]
        # arr_pos = [(val, idx) for idx, val in enumerate(arr_now)]
        # arr_pos.sort()
        # print(arr_pos)
        n = len(arr_pos)
        
        # print(arr_pos)

        visited = [False] * n
        swap_count = 0

        for i in range(n):
            if visited[i] or arr_pos[i][1] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr_pos[j][1]
                cycle_size += 1

            if cycle_size > 0:
                swap_count += (cycle_size - 1)

        return swap_count
