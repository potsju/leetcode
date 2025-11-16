class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maxval = max(nums)
        count= [0] * (maxval +1)
        for num in nums:
            count[num] +=1
        print(count)
        prefix = [0] * (maxval + 1)
        for i in range(1, maxval + 1):
            prefix[i] = prefix[i-1] + count[i-1] 
        print(prefix)
        return [prefix[num] for num in nums]