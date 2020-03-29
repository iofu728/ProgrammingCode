# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 10:30:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 10:36:00

"""
5368. Find Lucky Integer in an Array
User Accepted:1285
User Tried:1913
Total Accepted:1304
Total Submissions:2191
Difficulty:Easy
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

## Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

## Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

## Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

## Example 4:
Input: arr = [5]
Output: -1

## Example 5:
Input: arr = [7,7,7,7,7,7,7]
Output: 7

## Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500
"""
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for ii, jj in sorted(counter.items(), key=lambda i: -i[0]):
            if ii == jj:
                return ii
        return -1
