class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1][grid[0][0] % k] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                val = grid[i - 1][j - 1]
                for x in range(k):
                    new_r = (x + val) % k
                    dp[i][j][new_r] += (dp[i - 1][j][x] + dp[i][j - 1][x]) % MOD
                    
        return dp[m][n][0]