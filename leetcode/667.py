# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 22:30:45
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 22:31:25

"""
667. Beautiful Arrangement II Medium
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
Accepted 24,459 Submissions 45,013
"""


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        a, b = n - k - 1, k + 1
        max_list_a = list(range(1 + a, b // 2 + 2 + a))
        max_list_b = list(range(b + a, b // 2 + a, -1))
        max_list = [kk for ii, jj in zip(max_list_a, max_list_b) for kk in [ii, jj]]
        if b >> 1 << 1 != b:
            max_list = max_list[:-1]
        min_list = list(range(1, a + 1))
        # print(max_list, min_list)
        return min_list + max_list
