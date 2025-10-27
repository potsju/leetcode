class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def solve(p):
            b, s = (0, 0), (0, 0)
            for x in reversed(prices):
                s, b = max(s, (b[0] + x - p, b[1] + 1)), max(b, (s[0] - x, s[1]))
            return b
        l, r = 0, sum(prices)
        while l < r:
            m = (r + l + 1) // 2
            if solve(m)[1] >= k:
                l = m
            else:
                r = m - 1
        return solve(l)[0] + l * k