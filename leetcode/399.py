# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 20:29:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 20:29:38

"""
399. Evaluate Division Medium
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

Accepted 135,753 Submissions 261,893
"""
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        edges, done = defaultdict(dict), set()
        for (ii, jj), kk in zip(equations, values):
            edges[ii][jj] = kk
            edges[jj][ii] = 1 / kk
            if ii not in done and jj not in done:
                done.add(ii)
                done.add(jj)
            elif ii in done and jj in done:
                for d1 in edges[ii].keys():
                    for d2 in edges[jj].keys():
                        edges[d1][d2] = edges[d1][ii] * edges[ii][jj] * edges[jj][d2]
                        edges[d2][d1] = 1 / edges[d1][d2]
            elif ii in done:
                done.add(jj)
                for d in edges[ii].keys():
                    edges[jj][d] = edges[jj][ii] * edges[ii][d]
                    edges[d][jj] = 1 / edges[jj][d]
            elif jj in done:
                done.add(ii)
                for d in edges[jj].keys():
                    edges[ii][d] = edges[ii][jj] * edges[jj][d]
                    edges[d][ii] = 1 / edges[ii][d]
        res = []
        for ii, jj in queries:
            if not ii in done and not jj in done:
                res.append(-1.0)
            elif ii == jj:
                res.append(1.0)
            elif jj not in edges[ii]:
                res.append(-1.0)
            else:
                res.append(edges[ii][jj])
        return res
