class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        leftside = 0
        cases = 0
        for i in range(len(nums)):
            rightside = total - leftside - nums[i]
            if nums[i] ==0:
                if leftside == rightside:
                    cases+=2
                elif leftside == rightside-1 or leftside-1 == rightside:
                    cases+=1
            leftside += nums[i]
        return cases