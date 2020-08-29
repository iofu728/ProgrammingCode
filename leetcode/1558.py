# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 17:04:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 17:05:29


"""
1558. Minimum Numbers of Function Calls to Make Target Array Medium
Your task is to form an integer array nums from an initial array of zeros arr that is the same size as nums.

Return the minimum number of function calls to make nums from arr.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: nums = [1,5]
Output: 5
Explanation: Increment by 1 (second element): [0, 0] to get [0, 1] (1 operation).
Double all the elements: [0, 1] -> [0, 2] -> [0, 4] (2 operations).
Increment by 1 (both elements)  [0, 4] -> [1, 4] -> [1, 5] (2 operations).
Total of operations: 1 + 2 + 2 = 5.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Increment by 1 (both elements) [0, 0] -> [0, 1] -> [1, 1] (2 operations).
Double all the elements: [1, 1] -> [2, 2] (1 operation).
Total of operations: 2 + 1 = 3.
Example 3:

Input: nums = [4,2,5]
Output: 6
Explanation: (initial)[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,5](nums).
Example 4:

Input: nums = [3,2,2,4]
Output: 7
Example 5:

Input: nums = [2,4,8,16]
Output: 8
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
Accepted 6,086 Submissions 9,910
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def get_add_mul_times(num: int):
            a, b = 0, 0
            while num > 0:
                if num >> 1 << 1 != num:
                    a += 1
                    num -= 1
                else:
                    b += 1
                    num //= 2
            return a, b

        N = len(nums)
        add, mul = [0] * N, [0] * N
        for ii in range(N):
            a, b = get_add_mul_times(nums[ii])
            add[ii] = a
            mul[ii] = b
        return max(mul) + sum(add)
