class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c= Counter(nums)
        for key,value in c.items():
            if value == 1:
                return key
        return 1