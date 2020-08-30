# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 16:24:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 16:41:26

"""
853. Car Fleet Medium
N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.
Accepted 27,372 Submissions 64,654
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        res = N
        pairs = sorted(
            [(ii, jj) for ii, jj in zip(position, speed)], key=lambda i: i[0]
        )
        for ii in range(N):
            for jj in range(ii + 1, N):
                if pairs[jj][1] < pairs[ii][1] and (
                    pairs[jj][0] - pairs[ii][0]
                ) * pairs[jj][1] <= (target - pairs[jj][0]) * (
                    pairs[ii][1] - pairs[jj][1]
                ):
                    res -= 1
                    break
        return res
