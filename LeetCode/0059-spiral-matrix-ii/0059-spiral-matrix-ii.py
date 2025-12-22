class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]* n for _ in range(n)]
        row = n
        col = n
        x,y,dx,dy=0,0,1,0
        iter=1
        
        for _ in range(row * col):
            matrix[y][x] = iter 
            con1 = 0 <= y + dy < row
            con2 = 0 <=x + dx < col
            if not con1 or not con2 or matrix[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            x+=dx
            y+=dy
            iter+=1
        return matrix        

        
