# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-14 12:08:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-14 12:09:34

"""
1520. Maximum Number of Non-Overlapping Substrings Hard
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
Accepted 5,196 Submissions 15,507
"""
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        b, e = [-1] * 26, [-1] * 26
        for idx, ii in enumerate(s):
            t_id = ord(ii) - ord("a")
            if b[t_id] == -1:
                b[t_id] = idx
            e[t_id] = idx
        
        # print(b, e)
        for c in range(26):
            if b[c] == -1:
                continue
            ii = b[c]
            while ii <= e[c]:
                now_c = ord(s[ii]) - ord("a")
                if not (b[c] <= b[now_c] and e[now_c] <= e[c]):
                    b[c] = min(b[c], b[now_c])
                    e[c] = max(e[c], e[now_c])
                    ii = b[c]
                ii += 1
            # print(chr(c + ord("a")), b[c], e[c])
        pairs = [(jj, ii) for ii, jj in zip(b, e) if ii != -1]
        pairs = sorted(pairs, key=lambda i:(i[0], i[1] - i[0]))
        # print(pairs)
        pre = pairs[0]
        res = [pre]
        for ii in pairs[1:]:
            if ii[1] > pre[0]:
                pre = ii
                res.append(pre)
        return [s[ii:jj+1] for jj, ii in res]


