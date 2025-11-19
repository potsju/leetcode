class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums.sort()
        for n in nums:
            if original == n:
                original *=2
        return original