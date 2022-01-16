# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-15 14:52:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-15 14:52:38

"""
1345. Jump Game IV
Hard

1055

55

Add to List

Share
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108
Accepted
46,192
Submissions
108,514
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def dfs(idx, now):
            num = arr[idx]
            x = idxs[num][0]
        
        N = len(arr)
        idxs = defaultdict(list)
        for ii, jj in enumerate(arr):
            if N - 2 > ii > 0 and jj == arr[ii - 1] == arr[ii + 1]:
                continue
            idxs[jj].append(ii)
        queue = [(0, N - 1)]
        ka = set([N - 1])
        while queue:
            step, now = heapq.heappop(queue)
            # print(step, now, queue)
            if now == 0:
                return step
            num = arr[now]
            for ii in idxs[num]:
                if ii != now and ii not in ka:
                    heapq.heappush(queue, (step + 1, ii))
                    ka.add(ii)
            if now - 1 >= 0 and now - 1 not in ka:
                heapq.heappush(queue, (step + 1, now - 1))
                ka.add(now - 1)
            if now + 1 < N and now + 1 not in ka:
                heapq.heappush(queue, (step + 1, now + 1))
                ka.add(now + 1)
            idxs[num] = []