# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-06 17:53:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 17:54:38

"""
721. Accounts Merge Medium
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
Accepted 92,277 Submissions 187,468
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def get_root(r: list, p: int):
            q = r[p]
            while p != r[p]:
                p = r[p]
            while p != q:
                tmp = r[q]
                r[q] = p
                q = tmp
            return q

        N = len(accounts)
        ra = list(range(N))
        res, a_map = [set()] * N, {}
        for idx, ii in enumerate(accounts):
            have = set([get_root(ra, a_map[ii]) for ii in ii[1:] if ii in a_map])
            if not have:
                a_id = idx
                v = idx
            else:
                a_id = min(have)
                v = a_id
                # print(have, v)
                for jj in have:
                    if jj != a_id:
                        ra[jj] = v
                ra[idx] = v
                # print(ra)
            for jj in ii[1:]:
                a_map[jj] = v
        # print(ra)
        for ii in range(N):
            u = get_root(ra, ii)
            if u != ii:
                for jj in accounts[ii][1:]:
                    res[u].add(jj)
            else:
                res[ii] = set(accounts[ii][1:])
        return [ii[:1] + list(sorted(jj)) for ii, jj in zip(accounts, res) if jj]

