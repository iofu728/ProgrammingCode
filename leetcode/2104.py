"""
2104. Sum of Subarray Ranges
Medium

475

17

Add to List

Share
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109
 

Follow-up: Could you find a solution with O(n) time complexity?

Accepted
16,995
Submissions
28,458
"""


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        min_l, max_l = [0] * (N + 1), [0] * (N + 1)
        min_s, max_s = [], []
        min_res, max_res = 0, 0
        for ii, jj in enumerate(nums + [inf]):
            while max_s and nums[max_s[-1]] < jj:
                x = max_s.pop()
                max_res += (x - max_l[x]) * (ii - x) * nums[x]
            max_l[ii] = max_s[-1] if max_s else -1
            max_s.append(ii)
        for ii, jj in enumerate(nums + [-inf]):
            while min_s and nums[min_s[-1]] > jj:
                x = min_s.pop()
                min_res += (x - min_l[x]) * (ii - x) * nums[x]
            min_l[ii] = min_s[-1] if min_s else -1
            min_s.append(ii)
        return max_res - min_res
