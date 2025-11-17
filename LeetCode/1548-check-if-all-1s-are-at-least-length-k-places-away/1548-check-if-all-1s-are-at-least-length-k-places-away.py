class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos = []
        for i in range(len(nums)):
            if nums[i] == 1:
                pos.append(i)
        print(pos)
        for i in range(1,len(pos)):
            if pos[i]- pos[i-1]-1 < k:
                return False
        return True
            