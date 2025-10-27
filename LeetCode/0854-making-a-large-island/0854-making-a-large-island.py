class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        island_id = 2  # Start labeling islands from 2 to avoid confusion with 0 and 1
        area = {}  # island_id -> area size

        def dfs(r, c, id):
            # Out of bounds or not part of island
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = id
            return 1 + dfs(r + 1, c, id) + dfs(r - 1, c, id) + dfs(r, c + 1, id) + dfs(r, c - 1, id)

        # Step 1: Label each island and record its area
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # If the whole grid is one island already
        if not area:
            return 1
        res = max(area.values())

        # Step 2: Try flipping each 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    size = 1  # the flipped cell itself
                    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    for id in seen:
                        size += area[id]
                    res = max(res, size)

        return res
