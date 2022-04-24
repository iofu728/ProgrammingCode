"""
6044. 花期内花的数目 显示英文描述 
通过的用户数67
尝试过的用户数77
用户总通过次数68
用户总提交次数86
题目难度Hard
给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 starti 到 endi （都 包含）。同时给你一个下标从 0 开始大小为 n 的整数数组 persons ，persons[i] 是第 i 个人来看花的时间。

请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。

 

示例 1：



输入：flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
输出：[1,2,2,2]
解释：上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。
示例 2：



输入：flowers = [[1,10],[3,3]], persons = [3,3,2]
输出：[2,2,1]
解释：上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。
 

提示：

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= persons.length <= 5 * 104
1 <= persons[i] <= 109

"""
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        s = []
        for ii, jj in flowers:
            s.append((ii, 1))
            s.append((jj + 1, -1))
        s = sorted(s, key=lambda i:(i[0], i[1]))
        res = [0] * len(persons)
        persons = sorted(enumerate(persons), key=lambda i:(i[1], i[0]))
        now, idx, N = 0, 0, len(s)
        for ii, jj in persons:
            while idx < N and s[idx][0] <= jj:
                now += s[idx][1]
                idx += 1
            res[ii] = now
        return res
                
            

