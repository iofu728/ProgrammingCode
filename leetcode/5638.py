# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-27 11:27:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-27 11:40:40

"""
5638. 吃苹果的最大数目 显示英文描述 
通过的用户数520
尝试过的用户数1500
用户总通过次数522
用户总提交次数3375
题目难度Medium
有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。

你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。

给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。

 

示例 1：

输入：apples = [1,2,3,5,2], days = [3,2,1,4,2]
输出：7
解释：你可以吃掉 7 个苹果：
- 第一天，你吃掉第一天长出来的苹果。
- 第二天，你吃掉一个第二天长出来的苹果。
- 第三天，你吃掉一个第二天长出来的苹果。过了这一天，第三天长出来的苹果就已经腐烂了。
- 第四天到第七天，你吃的都是第四天长出来的苹果。
示例 2：

输入：apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
输出：5
解释：你可以吃掉 5 个苹果：
- 第一天到第三天，你吃的都是第一天长出来的苹果。
- 第四天和第五天不吃苹果。
- 第六天和第七天，你吃的都是第六天长出来的苹果。
 

提示：

apples.length == n
days.length == n
1 <= n <= 2 * 104
0 <= apples[i], days[i] <= 2 * 104
只有在 apples[i] = 0 时，days[i] = 0 才成立
"""
import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        res, day = 0, 1
        goods = [(days[0], apples[0])]
        while goods:
            # print(goods)
            d, a = heapq.heappop(goods)
            # print(day, d, a)
            while d < day:
                if goods:
                    d, a = heapq.heappop(goods)
                elif day < N:
                    heapq.heappush(goods, (days[day] + day, apples[day]))
                    day += 1
                    continue
                else:
                    # print("======")
                    break
            if d >= day:
                # print(day)
                res += 1
                if a > 1:
                    heapq.heappush(goods, (d, a - 1))
                if day < N:
                    heapq.heappush(goods, (days[day] + day, apples[day]))
            day += 1
        return res