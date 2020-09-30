# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 20:02:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 20:03:14

"""
1052. Grumpy Bookstore Owner Medium
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 

Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
Accepted 28,894 Submissions 52,088
"""


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)
        A = [0 if grumpy[ii] else customers[ii] for ii in range(N)]
        B = [
            0 if not customers[ii] or not grumpy[ii] else customers[ii]
            for ii in range(N)
        ]
        left = 1
        pre = sum(B[:X])
        max_p = pre
        # print(A, B)
        while left <= N - X:
            pre = pre - B[left - 1] + B[left + X - 1]
            max_p = max(max_p, pre)
            # print(left, max_p, pre)
            left += 1
        # print(sum(A), max_p)
        return sum(A) + max_p
