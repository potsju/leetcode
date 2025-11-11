class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp= [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            numzeros,numones = 0,0
            for a in s:
                if a == "1":
                    numones+=1
                else:
                    numzeros+=1
            for i in range(m, numzeros-1, -1):
                for j in range(n, numones-1,-1):
                    dp[i][j] = max(dp[i][j], dp[i-numzeros][j-numones]+1)
        return dp[m][n]