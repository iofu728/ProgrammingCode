# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 11:29:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-07 11:30:25

"""
347. Top K Frequent Elements Medium
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
Accepted 453,237 Submissions 737,904
"""
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], kk: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for k, v in c.items():
            if len(heap) > kk:
                heapq.heappop(heap)
            heapq.heappush(heap, (v, k))
        res = []
        while len(heap) > kk:
            heapq.heappop(heap)
        # print(len(heap), kk, heap)
        while heap:
            num, idx = heapq.heappop(heap)
            res.append(idx)
        return res
