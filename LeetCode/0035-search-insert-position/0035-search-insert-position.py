class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cur = 0
        for i in range(len(nums)):
            if target == nums[i]:
                cur = i
            elif target > nums[i]:
                cur = i+1
        return cur