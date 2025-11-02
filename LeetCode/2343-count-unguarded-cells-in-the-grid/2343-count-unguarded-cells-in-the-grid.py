class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        self.grid = [["."] * n for _ in range(m)]
        self.visited = set()

        # mark walls and guards
        for w in walls:
            self.grid[w[0]][w[1]] = "w"
        for g in guards:
            self.grid[g[0]][g[1]] = "g"

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        for g in guards:
            for dr, dc in dirs:
                self.dfs(g[0] + dr, g[1] + dc, dr, dc, self.visited, self.grid)

        count = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == ".":
                    count += 1
        return count

    def dfs(self, r, c, dr, dc, visited, grid):
        con1 = 0 <= r < len(grid)
        con2 = 0 <= c < len(grid[0])
        if not con1 or not con2:
            return
        if grid[r][c] in ("w", "g"):
            return

        grid[r][c] = "*"
        visited.add((r,c))

        self.dfs(r + dr, c + dc, dr, dc, visited, grid)
