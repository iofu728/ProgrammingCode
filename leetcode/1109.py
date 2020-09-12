# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-12 22:28:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-12 22:29:38

"""
1109. Corporate Flight Bookings Medium
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

 

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
 

Constraints:

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000
Accepted 19,379 Submissions 36,523
"""


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dp = [0] * n
        for ii, jj, kk in bookings:
            dp[ii - 1] += kk
            if jj < n:
                dp[jj] -= kk
        for ii in range(1, n):
            dp[ii] += dp[ii - 1]
        return dp
