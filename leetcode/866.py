class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_ok(n):
            return n > 1 and all(n % ii for ii in range(2, int(n ** 0.5) + 1))
        def is_reverse(n):
            k = str(n)
            l, r = 0, len(k) - 1
            while l < r:
                if k[l] != k[r]:
                    return False
                l += 1
                r -= 1
            return True
        while True:
            if is_reverse(n) and is_ok(n):
                return n
            n += 1
            if 10 ** 7 < n < 10 ** 8:
                n = 10 ** 8