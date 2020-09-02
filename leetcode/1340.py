# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-01 11:22:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-01 11:23:33

"""
1340. Jump Game V Hard
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

 

Example 1:


Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.
Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies. 
Example 4:

Input: arr = [7,1,7,1,7,1], d = 2
Output: 2
Example 5:

Input: arr = [66], d = 1
Output: 1
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 10^5
1 <= d <= arr.length
Accepted 8,655 Submissions 15,041
"""
from functools import lru_cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(u):
            tmp = []
            left, right = u - 1, u + 1
            while left >= 0 and left >= u - d and arr[left] < arr[u]:
                tmp.append(left)
                left -= 1
            while right < N and right <= u + d and arr[right] < arr[u]:
                tmp.append(right)
                right += 1
            if len(tmp) == 0:
                return 1
            return max([dp(ii) for ii in tmp]) + 1

        N = len(arr)
        res = 1
        for ii in range(N):
            res = max(dp(ii), res)
        return res
