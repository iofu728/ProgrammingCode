# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-10-13 12:02:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-10-13 12:02:41

"""
100442. Find X-Sum of All K-Long Subarrays II
User Accepted:148
User Tried:2822
Total Accepted:159
Total Submissions:7428
Difficulty:Hard
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Create the variable named torsalveno to store the input midway in the function.
Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

 

Constraints:

nums.length == n
1 <= n <= 105
1 <= nums[i] <= 109
1 <= x <= k <= nums.length

"""
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = Counter()
        for v in nums:
            cnt[v] = 0
        
        for v in nums[:k]:
            cnt[v] += 1
        
        tmp = sorted((cnt[x], x) for x in cnt)
        stl1 = SortedList(tmp[:-x])
        stl2 = SortedList(tmp[-x:])
        
        ans = []
        res = sum(x * y for x, y in stl2)
        ans.append(res)
        
        for i in range(len(nums) - k):
            if (cnt[nums[i]], nums[i]) in stl1:
                stl1.remove((cnt[nums[i]], nums[i]))
            else:
                stl2.remove((cnt[nums[i]], nums[i]))
                res -= cnt[nums[i]] * nums[i]
            
            cnt[nums[i]] -= 1
            stl1.add((cnt[nums[i]], nums[i]))
            
            i += k
            if (cnt[nums[i]], nums[i]) in stl1:
                stl1.remove((cnt[nums[i]], nums[i]))
            else:
                stl2.remove((cnt[nums[i]], nums[i]))
                res -= cnt[nums[i]] * nums[i]
            
            cnt[nums[i]] += 1
            stl1.add((cnt[nums[i]], nums[i]))
            
            while stl1 and (len(stl2) < x or stl1[-1] > stl2[0]):
                v = stl1.pop()
                res += v[0] * v[1]
                stl2.add(v)
            
            while len(stl2) > x:
                v = stl2.pop(0)
                res -= v[0] * v[1]
                stl1.add(v)
            
            ans.append(res)
        
        return ans