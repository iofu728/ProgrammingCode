# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 20:22:49
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 20:24:43

"""
1125. Smallest Sufficient Team Hard
In a project, you have a list of required skills req_skills, and a list of people.  The i-th person people[i] contains a list of skills that person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill.  We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= people.length <= 60
1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
Elements of req_skills and people[i] are (respectively) distinct.
req_skills[i][j], people[i][j][k] are lowercase English letters.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
Accepted 8,760 Submissions 18,829
"""


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        N, M = len(req_skills), len(people)
        NN = 1 << N
        skill2id = {jj: ii for ii, jj in enumerate(req_skills)}
        team = {ii: [] for ii in range(NN)}
        dp = [-1] * NN
        dp[0] = 0

        for ii in range(M):
            idx = 0
            for s in people[ii]:
                if s in skill2id:
                    idx = idx | (1 << skill2id[s])
            for jj in range(NN):
                if dp[jj] < 0:
                    continue
                x = jj | idx
                if dp[x] == -1 or dp[x] > dp[jj] + 1:
                    # print(ii, jj, x, team)
                    dp[x] = dp[jj] + 1
                    team[x] = team[jj].copy()
                    team[x].append(ii)
        # print(team)
        return team[NN - 1]
