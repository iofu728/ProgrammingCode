# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-08 12:31:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-08 12:32:05


"""
1105. Filling Bookcase Shelves Medium
We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

We want to place these books in order onto bookcase shelves that have total width shelf_width.

We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

 

Example 1:


Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
 

Constraints:

1 <= books.length <= 1000
1 <= books[i][0] <= shelf_width <= 1000
1 <= books[i][1] <= 1000
Accepted 17,350 Submissions 29,989
"""


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        N = len(books)
        dp = [10 ** 9 + 7] * (N + 1)
        dp[0] = 0
        for ii in range(1, N + 1):
            h, jj, tmp = 0, ii, 0
            while jj > 0:
                tmp += books[jj - 1][0]
                if tmp > shelf_width:
                    break
                h = max(h, books[jj - 1][1])
                dp[ii] = min(dp[ii], dp[jj - 1] + h)
                jj -= 1
        return dp[-1]
