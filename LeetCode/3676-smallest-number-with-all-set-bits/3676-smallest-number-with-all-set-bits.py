class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 2
        iter=1
        cur = 0
        while cur <= n:
            cur = pow(2,iter)
            iter+=1
        return cur-1