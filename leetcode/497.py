# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-06-21 21:00:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-06-22 09:12:12

"""
497. Random Point in Non-overlapping Rectangles Medium
Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]
Example 2:

Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

Accepted 12,302 Submissions 32,819
"""
import random


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.lens = [ii[2] - ii[0] + 1 for ii in rects]
        self.weights = [ii[3] - ii[1] + 1 for ii in rects]
        self.areas = [ii * jj for ii, jj in zip(self.lens, self.weights)]
        s_areas, tmp = [], 0
        for ii in self.areas:
            tmp += ii
            s_areas.append(tmp)
        self.s_areas = s_areas
        self.N = len(rects)
        # print(self.s_areas)

    def get_random(self):
        now_id = random.randint(0, self.s_areas[-1] - 1)
        area_id = 0
        for jj, ii in enumerate(self.s_areas[::-1]):
            if now_id < ii:
                area_id = self.N - jj - 1
        # print(now_id)
        return now_id - (self.s_areas[area_id - 1] if area_id else 0), area_id

    def pick(self) -> List[int]:
        now_id, area_id = self.get_random()
        # print(now_id, area_id)
        x1, y1, x2, y2 = self.rects[area_id]
        now_len, now_weight = self.lens[area_id], self.weights[area_id]
        x = x1 + now_id % now_len
        y = y1 + now_id // now_len
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()


def valid_num(a):
    phone = False

    total = 0
    if not a.isdigit():
        return phone
    count = len(set(list(a)))
    numbers = [int(ii) for ii in a]

    if (len(numbers) in [8, 9]) and count >= 3:
        if sum(numbers) == 10 * numbers[-2] + numbers[-1]:
            phone = True
    return phone
