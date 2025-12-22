class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        heap= [(grid[0][0], 0,0)]
        visited = set()
        visited.add((0,0))
        directions =[(0,1), (0,-1), (1,0), (-1,0)]
    
        while heap:
            time, x,y = heapq.heappop(heap)
            if (x,y)==(len(grid)-1,len(grid[0])-1):
                return time
            for d in directions:
                nx = x + d[0]
                ny = y + d[1]
                
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    heapq.heappush(heap, (max(time,grid[nx][ny],
                    time),nx,ny))