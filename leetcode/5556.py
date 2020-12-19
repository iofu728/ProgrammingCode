# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-11-01 11:05:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-11-01 11:28:11

"""
5556. 可以到达的最远建筑 显示英文描述 
通过的用户数249
尝试过的用户数344
用户总通过次数249
用户总提交次数425
题目难度Medium
给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。

你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。

当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：

如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
 

示例 1：


输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
输出：4
解释：从建筑物 0 出发，你可以按此方案完成旅程：
- 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
- 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
- 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
- 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
无法越过建筑物 4 ，因为没有更多砖块或梯子。
示例 2：

输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
输出：7
示例 3：

输入：heights = [14,3,19,3], bricks = 17, ladders = 0
输出：3
 

提示：

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
"""
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        need = [
            heights[ii] - heights[ii - 1] if heights[ii] > heights[ii - 1] else 0
            for ii in range(1, N)
        ]
        dp, idx = [], 0
        while idx < N - 1 and need[idx] <= bricks:
            if need[idx] > 0:
                heapq.heappush(dp, -1 * need[idx])
            bricks -= need[idx]
            idx += 1
        while ladders > 0 and idx < N - 1:
            if dp:
                tmp = heapq.heappop(dp)
                if -1 * tmp > need[idx]:
                    bricks += -1 * tmp - need[idx]
                    ladders -= 1
                    heapq.heappush(dp, -1 * need[idx])
                else:
                    ladders -= 1
                    heapq.heappush(dp, tmp)
            else:
                ladders -= 1
                heapq.heappush(dp, -1 * need[idx])
            idx += 1
            # print(111, idx)
            while idx < N - 1 and need[idx] <= bricks:
                if need[idx] > 0:
                    heapq.heappush(dp, -1 * need[idx])
                bricks -= need[idx]
                idx += 1
            # print(222, idx)
        return idx

