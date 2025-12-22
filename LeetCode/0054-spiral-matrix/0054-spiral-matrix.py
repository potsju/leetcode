class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        x,y,dx,dy= 0,0,1,0
        for pos in range(n * m):
            ans.append(matrix[y][x])
            matrix[y][x] = "."
            con1=0 <= x + dx < m
            con2= 0 <= y +dy < n
            if not con1 or not con2 or matrix[y+dy][x+dx]== ".":
                dx,dy = -dy, dx
            x+=dx
            y+=dy

        return ans
