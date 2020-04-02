# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-02 16:13:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-02 16:14:22

"""
面试题 17.18. Shortest Supersequence LCCI
You are given two arrays, one shorter (with all distinct elements) and one longer. Find the shortest subarray in the longer array that contains all the elements in the shorter array. The items can appear in any order.

Return the indexes of the leftmost and the rightmost elements of the array. If there are more than one answer, return the one that has the smallest left index. If there is no answer, return an empty array.

## Example 1:
Input:
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
Output: [7,10]

## Example 2:
Input:
big = [1,2,3]
small = [4]
Output: []

## Note:
big.length <= 100000
1 <= small.length <= 100000 
通过次数558提交次数1,373
"""
from collections import Counter


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        def is_in(a: dict, b: dict) -> bool:
            for key, value in a.items():
                if key not in b or value > b[key]:
                    return False
            return True

        N, M = len(big), len(small)
        left, right = 0, M
        have, need = Counter(big[:M]), Counter(small)
        min_num = [0, N]
        if is_in(need, have):
            return [0, M - 1]
        while left <= right and right < N and left >= 0:
            tt = left
            while right < N and not is_in(need, have):
                have[big[right]] = have.get(big[right], 0) + 1
                right += 1
            while left < right and is_in(need, have):
                have[big[left]] -= 1
                if not have[big[left]]:
                    del have[big[left]]
                left += 1
            t = left - 1 if left != tt else tt
            # print(left, right, t)
            if min_num[1] - min_num[0] > right - t - 1 and (tt != left):
                min_num = [t, right - 1]
        if min_num == [0, N]:
            min_num = []
        return min_num
