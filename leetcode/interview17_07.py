# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-10 11:06:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-10 11:06:22

"""
面试题 17.07. 婴儿名字
每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。

在结果列表中，选择字典序最小的名字作为真实名字。

示例：

输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]
提示：

names.length <= 100000
通过次数3,269提交次数8,269
"""
class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        def get_root(r: list, p: int):
            q = r[p]
            while p != r[p]:
                p = r[p]
            while p != q:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p
        N = len(names)
        name_map = {ii[:ii.find("(")]: idx for idx,ii in enumerate(names)}
        idx2name = {v:k for k, v in name_map.items()}
        nums = {}
        dp = list(range(N))
        for s in synonyms:
            ii, jj = s[1:-1].split(",")
            if ii > jj:
                jj, ii = ii, jj
            if ii not in name_map:
                name_map[ii] = len(name_map)
                idx2name[name_map[ii]] = ii
                dp = dp + [len(dp)]
            if jj not in name_map:
                name_map[jj] = len(name_map)
                idx2name[name_map[jj]] = jj
                dp = dp + [len(dp)]
            v = get_root(dp, name_map[jj])
            u = get_root(dp, name_map[ii])
            if idx2name[u] > idx2name[v] and v < N:
                dp[u] = v
            else:
                dp[v] = u
            # print(dp, name_map[ii], name_map[jj])
        for ii, jj in zip(dp, names):
            ii = get_root(dp, ii)
            now = int(jj[jj.find("(") + 1:-1])
            nums[ii] = nums.get(ii, 0) + now
        # return dp, names, name_map, nums
        return ["{}({})".format(idx2name[idx], nums[idx]) for idx, ii in enumerate(dp) if idx < N and idx == ii]