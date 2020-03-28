# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-28 00:26:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-28 00:43:49

"""
820. Short Encoding of Words Medium

Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

## Example:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].

## Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.
Accepted 11,904 Submissions 23,990
"""


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(words, key=lambda i: -len(i))
        cache = {}
        for ii in words:
            if ii[-1] not in cache:
                cache[ii[-1]] = {}
            in_cache = [k for k in cache[ii[-1]].keys() if ii in k]
            if not len(in_cache):
                cache[ii[-1]][ii] = [ii]
            else:
                cache[ii[-1]][in_cache[-1]].append(ii)
        # print(cache)
        need = [kk for k, v in cache.items() for kk in v.keys()]
        return sum([len(ii) for ii in need]) + len(need)
