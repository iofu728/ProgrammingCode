"""
2055. Plates Between Candles
Medium

339

8

Add to List

Share
There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

 

Example 1:

ex-1
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.
Example 2:

ex-2
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.
 

Constraints:

3 <= s.length <= 105
s consists of '*' and '|' characters.
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length
Accepted
9,079
Submissions
19,315
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        def get(v, is_left=True):
            idx = bisect.bisect_left(s_s, v)
            if not is_left:
                if idx < len(s_s) and s_s[idx] > v:
                    idx -= 1
                elif idx >= len(s_s):
                    idx -= 1
            return s_s[idx] if 0 <= idx < len(s_s) else -1

        pre = 0
        s_s, s_map = [], {}
        for ii, jj in enumerate(s):
            if jj == "|":
                s_s.append(ii)
                s_map[ii] = pre
            else:
                pre += 1
        res = []
        # print(s_s)
        for ii, jj in queries:
            l = get(ii)
            r = get(jj, False)
            # print(l, r)
            if l == -1 or r == -1:
                tmp = 0
            else:
                tmp = s_map.get(r, 0) - s_map.get(l, 0)
            res.append(tmp if tmp >= 0 else 0)
        return res
