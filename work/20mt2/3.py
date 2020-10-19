
import sys
import heapq

T = int(sys.stdin.readline())

def get_seat():
    N = int(sys.stdin.readline())
    s1, s2 = [], []
    for jj, ii in enumerate(sys.stdin.readline().strip()):
        if ii == "1":
            heapq.heappush(s1, jj)
        elif ii == "0":
            heapq.heappush(s2, jj)
    M = int(sys.stdin.readline())
    for ii in sys.stdin.readline().strip():
        if ii == "M":
            if s1:
                idx = heapq.heappop(s1)
            else:
                idx = heapq.heappop(s2)
                heapq.heappush(s1, idx)
        else:
            if s2:
                idx = heapq.heappop(s2)
                heapq.heappush(s1, idx)
            else:
                idx = heapq.heappop(s1)
        print(str(idx + 1))


for _ in range(T):
    get_seat()