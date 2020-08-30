# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 20:58:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 20:59:17

"""
1169. Invalid Transactions Medium
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
Accepted 16,480 Submissions 52,861
"""
from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        store = defaultdict(dict)
        res = []
        have = set()
        for ii in transactions:
            name, times, v, city = ii.split(",")
            if int(v) > 1000:
                res.append(ii)
                have.add((name, int(times), int(v), city))
            if city not in store[name]:
                store[name][city] = []
            store[name][city].append((int(times), int(v)))

        for name, v_list in store.items():
            if len(v_list) <= 1:
                continue
            for c1 in v_list.keys():
                for c2 in v_list.keys():
                    if c1 == c2:
                        continue
                    for t1, v1 in v_list[c1]:
                        # if (name, t1, v1, c1) in have:
                        #     continue
                        for t2, v2 in v_list[c2]:
                            if (name, t2, v2, c2) in have:
                                continue
                            # print(t1, t2)
                            if abs(t1 - t2) <= 60:
                                if (name, t2, v2, c2) not in have:
                                    res.append(",".join([name, str(t2), str(v2), c2]))
                                    have.add((name, t2, v2, c2))
                                if (name, t1, v1, c1) not in have:
                                    res.append(",".join([name, str(t1), str(v1), c1]))
                                    have.add((name, t1, v1, c1))

        return res
