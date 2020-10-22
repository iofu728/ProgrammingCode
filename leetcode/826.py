# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-22 01:11:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-22 01:12:54

"""
826. Most Profit Assigning Work Medium
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
Notes:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
Accepted 22,319 Submissions 57,644
"""

import bisect
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        g = {}
        for ii, jj in zip(difficulty, profit):
            if ii in g:
                g[ii] = max(g[ii], jj)
            else:
                g[ii] = jj
        pre = 0
        for ii in sorted(g.keys()):
            g[ii] = max(g[ii], pre)
            pre = max(pre, g[ii])
        d = []
        for ii in difficulty:
            bisect.insort(d, ii)
        res = 0
        # print(d)
        for ii in worker:
            tmp = bisect.bisect_right(d, ii) - 1
            # print(ii, d[tmp])
            if tmp >= 0:
                res += g[d[tmp]]
        return res
