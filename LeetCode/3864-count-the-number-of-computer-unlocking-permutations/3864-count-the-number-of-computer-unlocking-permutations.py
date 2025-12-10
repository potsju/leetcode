class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        for i in range(1,len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
        ans = 1
        mod = pow(10,9) + 7
        
        for i in range(2,len(complexity)):
            ans = ans * i % mod
        return ans