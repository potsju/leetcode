class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for n in nums:
            if (n %3) !=0:
                sum +=1
    
            
        return sum