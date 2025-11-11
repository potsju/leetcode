class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        NEG = -10**18
        # dp[i][j] will be an array length k+1, but we only keep previous row and current row to save memory.
        # However for clarity, implement full 2D arrays of arrays.
        dp = [[[NEG] * (k + 1) for _ in range(n)] for __ in range(m)]

        # cost contributed by a cell (1 if non-zero, else 0)
        def cost_of(val):
            return 1 if val != 0 else 0

        # initialize (0,0)
        c0 = cost_of(grid[0][0])
        if c0 <= k:
            dp[0][0][c0] = grid[0][0]

        # first row (can only come from left)
        for j in range(1, n):
            curc = cost_of(grid[0][j])
            for prev_c in range(k + 1):
                if dp[0][j-1][prev_c] != NEG:
                    newc = prev_c + curc
                    if newc <= k:
                        dp[0][j][newc] = max(dp[0][j][newc], dp[0][j-1][prev_c] + grid[0][j])

        # first column (can only come from top)
        for i in range(1, m):
            curc = cost_of(grid[i][0])
            for prev_c in range(k + 1):
                if dp[i-1][0][prev_c] != NEG:
                    newc = prev_c + curc
                    if newc <= k:
                        dp[i][0][newc] = max(dp[i][0][newc], dp[i-1][0][prev_c] + grid[i][0])

        # rest of grid
        for i in range(1, m):
            for j in range(1, n):
                curc = cost_of(grid[i][j])
                # from top
                for prev_c in range(k + 1):
                    if dp[i-1][j][prev_c] != NEG:
                        newc = prev_c + curc
                        if newc <= k:
                            dp[i][j][newc] = max(dp[i][j][newc], dp[i-1][j][prev_c] + grid[i][j])
                # from left
                for prev_c in range(k + 1):
                    if dp[i][j-1][prev_c] != NEG:
                        newc = prev_c + curc
                        if newc <= k:
                            dp[i][j][newc] = max(dp[i][j][newc], dp[i][j-1][prev_c] + grid[i][j])

        # answer: best score at bottom-right with cost <= k
        ans = max(dp[m-1][n-1])
        return ans if ans != NEG else -1
