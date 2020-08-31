# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 13:06:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 13:07:18

"""
710. Random Pick with Blacklist Hard
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
Example 2:

Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
Example 3:

Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
Example 4:

Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

Accepted 13,617 Submissions 41,914
"""


class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        write_len = N - len(blacklist)
        self.write_len = write_len
        w = set([ii for ii in range(write_len, N)])
        for ii in blacklist:
            if ii >= write_len:
                w.remove(ii)
        w = list(w)
        idx = 0
        self.write_map = {}
        for ii in blacklist:
            if ii < write_len:
                self.write_map[ii] = w[idx]
                idx += 1

    def pick(self) -> int:
        k = random.randint(0, self.write_len - 1)
        return self.write_map.get(k, k)

