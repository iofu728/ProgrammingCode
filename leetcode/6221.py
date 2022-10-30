# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-30 11:09:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-30 11:09:54

"""
6221. 最流行的视频创作者 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你两个字符串数组 creators 和 ids ，和一个整数数组 views ，所有数组的长度都是 n 。平台上第 i 个视频者是 creator[i] ，视频分配的 id 是 ids[i] ，且播放量为 views[i] 。

视频创作者的 流行度 是该创作者的 所有 视频的播放量的 总和 。请找出流行度 最高 创作者以及该创作者播放量 最大 的视频的 id 。

如果存在多个创作者流行度都最高，则需要找出所有符合条件的创作者。
如果某个创作者存在多个播放量最高的视频，则只需要找出字典序最小的 id 。
返回一个二维字符串数组 answer ，其中 answer[i] = [creatori, idi] 表示 creatori 的流行度 最高 且其最流行的视频 id 是 idi ，可以按任何顺序返回该结果。

 

示例 1：

输入：creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
输出：[["alice","one"],["bob","two"]]
解释：
alice 的流行度是 5 + 5 = 10 。
bob 的流行度是 10 。
chris 的流行度是 4 。
alice 和 bob 是流行度最高的创作者。
bob 播放量最高的视频 id 为 "two" 。
alice 播放量最高的视频 id 是 "one" 和 "three" 。由于 "one" 的字典序比 "three" 更小，所以结果中返回的 id 是 "one" 。
示例 2：

输入：creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]
输出：[["alice","b"]]
解释：
id 为 "b" 和 "c" 的视频都满足播放量最高的条件。
由于 "b" 的字典序比 "c" 更小，所以结果中返回的 id 是 "b" 。
 

提示：

n == creators.length == ids.length == views.length
1 <= n <= 105
1 <= creators[i].length, ids[i].length <= 5
creators[i] 和 ids[i] 仅由小写英文字母组成
0 <= views[i] <= 105
"""
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        c1, c2 = {}, defaultdict(int)
        for ii, jj, kk in zip(creators, ids, views):
            c2[ii] += kk
            if ii in c1:
                if c1[ii][-1] < kk or (c1[ii][-1] == kk and c1[ii][0] > jj):
                    c1[ii] = (jj, kk)
            else:
                c1[ii] = (jj, kk)
        m = max(c2.values())
        return [[ii, c1[ii][0]] for ii, jj in c2.items() if jj == m]
            
            