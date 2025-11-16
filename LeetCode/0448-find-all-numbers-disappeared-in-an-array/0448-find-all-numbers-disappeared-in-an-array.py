class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        original =[]
        for i in range(1,len(nums)+1):
            original.append(i)
        arr= []
        nums.sort()
        for i in range(len(nums)):
            if original[i] not in nums:
                arr.append(original[i])
        return arr