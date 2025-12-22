class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) >= 1 and len(grid[0]) >=1 and grid[0][1] >1 and grid[1][0] > 1:
            return -1
        heap = [(0, 0,0)]
        directions = [(0,1), (0, -1), (-1,0), (1,0)]
        visited = set()
        while heap:
            time, x,y = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if x == len(grid)-1 and y == len(grid[0])-1:
                return time
            for d in directions:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx,ny) not in visited:
                    if grid[nx][ny] <= time+1:
                        next_time = time+1
                    elif (grid[nx][ny] - time) % 2 == 1:
                        next_time = grid[nx][ny]
                    elif (grid[nx][ny] - time) % 2 == 0:
                        next_time = grid[nx][ny]+1
                    heapq.heappush(heap,(next_time, nx,ny))
        return -1
        