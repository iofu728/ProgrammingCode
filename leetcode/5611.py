import heapq

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        queue = [(-1 * abs(ii + jj), ii, jj) for ii, jj in zip(aliceValues, bobValues)]
        heapq.heapify(queue)
        # print(queue)
        a, b = 0, 0
        while queue:
            _, ii, _ = heapq.heappop(queue)
            a += ii
            if queue:
                _, _, jj = heapq.heappop(queue)
                b += jj
        # print(a, b)
        return 0 if a == b else (1 if a > b else -1)