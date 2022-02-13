"""
1405. Longest Happy String
Medium

935

162

Add to List

Share
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
Accepted
34,190
Submissions
61,396
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        for ii, jj in zip(["a", "b", "c"], [a, b, c]):
            if jj > 0:
                heapq.heappush(q, (-jj, ii))
        res = []
        while q:
            num, now = heapq.heappop(q)
            if len(res) >= 2 and len(set(res[-2:] + [now])) == 1:
                if not q:
                    break
                x, y = heapq.heappop(q)
                res.append(y)
                if -x > 1:
                    heapq.heappush(q, (x + 1, y))
                heapq.heappush(q, (num, now))
            else:
                res.append(now)
                if -num > 1:
                    heapq.heappush(q, (num + 1, now))
        return "".join(res)
