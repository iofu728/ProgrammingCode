# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-24 18:26:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-24 18:27:49

"""
1024. Video Stitching Medium
You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.

 

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation: 
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
Example 2:

Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation: 
We can't cover [0,5] with only [0,1] and [1,2].
Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation: 
We can take clips [0,4], [4,7], and [6,9].
Example 4:

Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation: 
Notice you can have extra video after the event ends.
 

Constraints:

1 <= clips.length <= 100
0 <= clips[i][0] <= clips[i][1] <= 100
0 <= T <= 100
Accepted 26,546 Submissions 53,808
"""


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0
        N = len(clips)
        clips = sorted(clips, key=lambda i: (i[0], -i[1]))
        # print(clips)
        if clips[0][0] != 0:
            return -1
        e = clips[0][1]
        res, idx, pre = 1, 0, 1
        while e < T and idx < N:
            if (idx + 1 < N and clips[idx + 1][0] > e and e < T) or (
                idx == N - 1 and e < T
            ):
                return -1
            while idx + 1 < N and clips[idx + 1][0] <= e:
                idx += 1
                if clips[pre][1] < clips[idx][1]:
                    pre = idx
            res += 1
            e = clips[pre][1]
            # print(idx, e)
        if e < T:
            return -1
        return res
