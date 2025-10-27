class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum, maxsum = 0, -sys.maxsize
        sums= 0
        for i in range(len(nums)):
            sums += nums[i]
            cursum += nums[i]
            maxsum =max(cursum, maxsum)
            if cursum < 0:
                cursum =0
        cursum =0
        max2=0
        for i in range(len(nums)):
            maxsum = max(maxsum, sums + max2)
            sums -= nums[i]
            cursum += nums[i]
            max2 = max(max2, cursum)
        return maxsum