# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 21:26:49
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 21:27:35

"""
207. Course Schedule Medium
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
Accepted 449,299 Submissions 1,039,035
"""
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(ii: int):
            flag[ii] = 1
            for v in edges[ii]:
                if flag[v] == 0:
                    dfs(v)
                    if not self.valid:
                        return
                elif flag[v] == 1:
                    self.valid = False
                    return
            flag[ii] = 2
            res.append(ii)

        res = []
        edges = defaultdict(list)
        flag = [0] * numCourses
        self.valid = True
        for ii, jj in prerequisites:
            edges[ii].append(jj)
        for ii in range(numCourses):
            if self.valid and flag[ii] == 0:
                dfs(ii)
        return self.valid
