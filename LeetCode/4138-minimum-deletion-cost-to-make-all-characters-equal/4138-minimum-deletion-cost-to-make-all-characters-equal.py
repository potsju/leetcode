class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        total = 0
        for i in range(len(s)):
            d[s[i]] += cost[i]
            total += cost[i]
        return total - max(d.values())