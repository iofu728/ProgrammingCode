# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-07-16 11:42:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-07-16 11:42:59

"""
6927. 合法分割的最小下标 显示英文描述 
通过的用户数83
尝试过的用户数91
用户总通过次数83
用户总提交次数97
题目难度Medium
如果元素 x 在长度为 m 的整数数组 arr 中满足 freq(x) * 2 > m ，那么我们称 x 是 支配元素 。其中 freq(x) 是 x 在数组 arr 中出现的次数。注意，根据这个定义，数组 arr 最多 只会有 一个 支配元素。

给你一个下标从 0 开始长度为 n 的整数数组 nums ，数据保证它含有一个支配元素。

你需要在下标 i 处将 nums 分割成两个数组 nums[0, ..., i] 和 nums[i + 1, ..., n - 1] ，如果一个分割满足以下条件，我们称它是 合法 的：

0 <= i < n - 1
nums[0, ..., i] 和 nums[i + 1, ..., n - 1] 的支配元素相同。
这里， nums[i, ..., j] 表示 nums 的一个子数组，它开始于下标 i ，结束于下标 j ，两个端点都包含在子数组内。特别地，如果 j < i ，那么 nums[i, ..., j] 表示一个空数组。

请你返回一个 合法分割 的 最小 下标。如果合法分割不存在，返回 -1 。

 

示例 1：

输入：nums = [1,2,2,2]
输出：2
解释：我们将数组在下标 2 处分割，得到 [1,2,2] 和 [2] 。
数组 [1,2,2] 中，元素 2 是支配元素，因为它在数组中出现了 2 次，且 2 * 2 > 3 。
数组 [2] 中，元素 2 是支配元素，因为它在数组中出现了 1 次，且 1 * 2 > 1 。
两个数组 [1,2,2] 和 [2] 都有与 nums 一样的支配元素，所以这是一个合法分割。
下标 2 是合法分割中的最小下标。
示例 2：

输入：nums = [2,1,3,1,1,1,7,1,2,1]
输出：4
解释：我们将数组在下标 4 处分割，得到 [2,1,3,1,1] 和 [1,7,1,2,1] 。
数组 [2,1,3,1,1] 中，元素 1 是支配元素，因为它在数组中出现了 3 次，且 3 * 2 > 5 。
数组 [1,7,1,2,1] 中，元素 1 是支配元素，因为它在数组中出现了 3 次，且 3 * 2 > 5 。
两个数组 [2,1,3,1,1] 和 [1,7,1,2,1] 都有与 nums 一样的支配元素，所以这是一个合法分割。
下标 4 是所有合法分割中的最小下标。
示例 3：

输入：nums = [3,3,3,3,7,2,2]
输出：-1
解释：没有合法分割。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
nums 有且只有一个支配元素。
"""
from sortedcontainers import SortedList

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def is_ok(a, n):
            b = a[0]
            return b * 2 > n
            
        c1, c2 = Counter(), Counter(nums)
        s1, s2 = SortedList([]), SortedList([(jj, ii) for ii, jj in sorted(c2.items(), key=lambda i:(i[1], i[0]))])
        N = len(nums)
        for ii in range(N - 1):
            y = nums[ii]
            c1[y] += 1
            if (c1[y] - 1, y) in s1:
                s1.remove((c1[y] - 1, y))
            s1.add((c1[y], y))

            c2[y] -= 1
            s2.remove((c2[y] + 1, y))
            s2.add((c2[y], y))
            # print(s1[-1], s2[-1], ii + 1, N - ii - 1)
            if not is_ok(s1[-1], ii + 1) or not is_ok(s2[-1], N - ii - 1):
                continue
            a1, b1 = s1[-1][1], s2[-1][1]
            if a1 == b1:
                return ii
        return -1