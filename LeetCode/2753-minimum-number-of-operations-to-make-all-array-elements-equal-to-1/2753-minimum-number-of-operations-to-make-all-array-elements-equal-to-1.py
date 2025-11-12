class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n- ones
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i+1,n):
                a,b = g, nums[j]
                while b:
                    a, b = b, a % b
                g =a
                if g == 1:
                    min_len = min(min_len,j-i+1)
                    break
        if min_len == float('inf'):
            return -1
        return (min_len -1) + (n-1)