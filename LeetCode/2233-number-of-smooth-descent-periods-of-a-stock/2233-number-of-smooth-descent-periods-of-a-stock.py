class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prev = prices[0]
        streak=1
        ans=0
        if len(prices) == 1:
            return 1
        for i in range(1,len(prices)):
            print(prices[i], prev)
            if prices[i] !=  prev-1:
                ans += ((streak * (streak+1))/2) 
                streak=1
                prev = prices[i]
                continue

            streak+=1
            prev = prices[i]
        ans += (streak * (streak+1))/2
        return ans