class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        N = len(word)
        idx = 1
        while idx * k < N:
            if word[idx * k:] == word[:N - idx * k]:
                return idx
            idx += 1
        return idx
