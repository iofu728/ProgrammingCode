# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 10:37:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 10:45:21

"""
5178. Four Divisors
User Accepted:681
User Tried:1260
Total Accepted:696
Total Submissions:1767
Difficulty:Medium
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
 

Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5

"""

from math import sqrt
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def factorization(num: int):
            factor = [1, num]
            for ii in range(2, int(sqrt(num)) + 1):
                if num % ii == 0:
                    factor.append(ii)
                    if int(num / ii) > ii:
                        factor.append(int(num / ii))
                    if len(factor) > 4:
                        return []
            return factor
        factors = [factorization(ii) for ii in nums]
        # print(factors)
        factors = [sum(ii) for ii in factors if len(ii) == 4]
        if len(factors) == 0:
            return 0
        return sum(factors)
        
        