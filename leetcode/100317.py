# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-16 11:44:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-16 11:44:43

"""
100317. 数组中的峰值 显示英文描述 
通过的用户数107
尝试过的用户数158
用户总通过次数112
用户总提交次数259
题目难度Hard
数组 arr 中 大于 前面和后面相邻元素的元素被称为 峰值 元素。

给你一个整数数组 nums 和一个二维整数数组 queries 。

你需要处理以下两种类型的操作：

queries[i] = [1, li, ri] ，求出子数组 nums[li..ri] 中 峰值 元素的数目。
queries[i] = [2, indexi, vali] ，将 nums[indexi] 变为 vali 。
请你返回一个数组 answer ，它依次包含每一个第一种操作的答案。

注意：

子数组中 第一个 和 最后一个 元素都 不是 峰值元素。
 

示例 1：

输入：nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]

输出：[0]

解释：

第一个操作：我们将 nums[3] 变为 4 ，nums 变为 [3,1,4,4,5] 。

第二个操作：[3,1,4,4,5] 中峰值元素的数目为 0 。

示例 2：

输入：nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]

输出：[0,1]

解释：

第一个操作：nums[2] 变为 4 ，它已经是 4 了，所以保持不变。

第二个操作：[4,1,4] 中峰值元素的数目为 0 。

第三个操作：第二个 4 是 [4,1,4,2,1] 中的峰值元素。

 

提示：

3 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i][0] == 1 或者 queries[i][0] == 2
对于所有的 i ，都有：
queries[i][0] == 1 ：0 <= queries[i][1] <= queries[i][2] <= nums.length - 1
queries[i][0] == 2 ：0 <= queries[i][1] <= nums.length - 1, 1 <= queries[i][2] <= 105

"""
from sortedcontainers import SortedList

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        peaks = [nums[i] > nums[i - 1] and nums[i] > nums[i + 1] for i in range(1, len(nums) - 1)]
        peaks_sum = [0]
        for ii in peaks:
            peaks_sum.append(peaks_sum[-1] + ii)
        peaks_sum.append(peaks_sum[-1])
        # peaks_sum.append(peaks_sum[-1])
        answer = []
        changes_add = SortedList([])
        changes_remove = SortedList([])
        for query in queries:
            if query[0] == 1:
                li, ri = query[1], query[2]
                tmp = peaks_sum[ri - 1] - peaks_sum[li] if ri - 1 >= li else 0
                # print(changes_add, changes_remove)
                idx1 = changes_add.bisect_left(li + 1)
                idx2 = changes_add.bisect_right(ri - 1)
                idx3 = changes_remove.bisect_left(li + 1)
                idx4 = changes_remove.bisect_right(ri - 1)
                # print(tmp, idx1, idx2, idx3, idx4)
                answer.append(tmp + (idx2 - idx1 if idx2 >= idx1 else 0) + (idx3 - idx4 if idx4 >= idx3 else 0))
            elif query[0] == 2:
                index, val = query[1], query[2]
                nums[index] = val
                for i in [index - 1, index, index + 1]:
                    if not len(nums) - 1 > i > 0:
                        continue
                    now = nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
                    if now != peaks[i - 1]:
                        if now == 1:
                            changes_add.add(i)
                        else:
                            changes_remove.add(i)
                        peaks[i - 1] = now
                
        return answer