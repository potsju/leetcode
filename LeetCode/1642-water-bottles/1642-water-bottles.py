class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        emptybottles=0
        total = 0
        while numBottles >=numExchange:
            numBottles-=numExchange
            total +=numExchange
            numBottles+=1
        return total + numBottles