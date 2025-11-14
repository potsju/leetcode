class Solution(object):
    def rangeAddQueries(self, n, queries):
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # 2) Build the prefix sum to get final matrix
        # First horizontal prefix
        for r in range(n):
            for c in range(1, n):
                diff[r][c] += diff[r][c - 1]

        # Then vertical prefix
        for c in range(n):
            for r in range(1, n):
                diff[r][c] += diff[r - 1][c]

        # 3) Extract the n×n matrix                                                                                                                                                                                                                                                                                     
        result = [row[:n] for row in diff[:n]]
        return result
