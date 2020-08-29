# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-27 12:40:42
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-27 12:41:36

"""
332. Reconstruct Itinerary Medium
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
Accepted 168,454 Submissions 457,611
"""
from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while dirs[curr]:
                tmp = heapq.heappop(dirs[curr])
                dfs(tmp)
            res.append(curr)

        dirs = defaultdict(list)
        for ii, jj in tickets:
            # if ii not in dirs:
            #     dirs[ii] = []
            dirs[ii].append(jj)
        for key in dirs:
            heapq.heapify(dirs[key])
        now = "JFK"
        res = []
        dfs(now)
        # while True:
        #     if now not in dirs or not len(dirs[now]):
        #         break
        #     now = dirs[now].pop(0)
        #     res.append(now)
        return res[::-1]
