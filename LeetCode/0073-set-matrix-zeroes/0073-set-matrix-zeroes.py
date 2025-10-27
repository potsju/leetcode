class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rLen = len(matrix)
        cLen = len(matrix[0])
        rows = [False] * rLen
        cols = [False] * cLen
        for r in range(rLen):
            for c in range(cLen): # Traverse through matrix and save rows and cols that must be 0
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for i, r in enumerate(rows): # iterate through rows that must be 0 and set to 0
            if r:
                for c in range(cLen):
                    matrix[i][c] = 0
        for j, c in enumerate(cols): # iterate through cols that must be 0 and set to 0
            if c:
                for r in range(rLen):
                    matrix[r][j] = 0
        