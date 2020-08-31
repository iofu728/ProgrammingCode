# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 00:08:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 00:09:17

"""
841. Keys and Rooms Medium
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
Accepted 81,320 Submissions 126,043
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(u: int):
            flag[u] = 0
            for v in rooms[u]:
                if flag[v]:
                    dfs(v)

        N = len(rooms)
        flag = [1] * N
        dfs(0)
        # print(flag)
        return sum(flag) == 0
