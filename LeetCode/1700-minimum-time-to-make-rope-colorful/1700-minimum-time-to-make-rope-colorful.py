class Solution(object):
    def minCost(self, colors, time):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        s = 0
        for i in range(1,len(colors)):
            if colors[i]== colors[i-1]:
                s+= min(time[i], time[i-1])
                time[i] = max(time[i], time[i-1])
        print(time)
        return s