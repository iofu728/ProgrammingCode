# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-08 10:34:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-08 10:58:27

"""
5353. Bulb Switcher III
User Accepted:1356
User Tried:1866
Total Accepted:1811
Total Submissions:2897
Difficulty:Medium
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.

 

Example 1:



Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.
Example 2:

Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).
Example 3:

Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.
Example 4:

Input: light = [2,1,4,3,6,5]
Output: 3
Example 5:

Input: light = [1,2,3,4,5,6]
Output: 6
 

Constraints:

n == light.length
1 <= n <= 5 * 10^4
light is a permutation of  [1, 2, ..., n]
"""


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        same = 0
        finish, no_finish = {}, {}
        for ii in range(1, len(light) + 1):
            now = light[ii - 1]
            finish[now] = 0
            if ii not in finish:
                no_finish[ii] = 0
            if now in no_finish:
                del no_finish[now]
            if len(no_finish) == 0:
                same += 1
        return same

