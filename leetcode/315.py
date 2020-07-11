# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 10:34:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 10:35:43

"""
315. Count of Smaller Numbers After Self Hard
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Accepted 128,391 Submissions 310,778
"""


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        queue, res = [], []
        for ii in nums[::-1]:
            idx = bisect.bisect_left(queue, ii)
            res.append(idx)
            queue.insert(idx, ii)
        return res[::-1]
