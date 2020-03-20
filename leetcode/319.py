# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-20 12:27:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-20 12:45:55

"""
319. Bulb Switcher
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
通过次数8,700提交次数19,306
"""
import math


class Solution:
    def bulbSwitch(self, N: int) -> int:
        return int(math.sqrt(N))
