class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        N = n + k - 1
        R = 2 * k
        R = min(R, N - R)

        num = 1
        den = 1

        for i in range(1, R + 1):
            num = num * (N - R + i) % MOD
            den = den * i % MOD

        return num * pow(den, MOD - 2, MOD) % MOD