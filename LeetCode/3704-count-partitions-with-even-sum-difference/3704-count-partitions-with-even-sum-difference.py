class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum = nums[0]
        rightsum = sum(nums)-nums[0]
        ans = 0
        if abs(leftsum-rightsum) % 2 == 0:
            ans +=1
        for i in range(1, len(nums)-1):
            leftsum += nums[i]
            rightsum -= nums[i]
            if abs(leftsum-rightsum) % 2 == 0:
                ans+=1
        return ans