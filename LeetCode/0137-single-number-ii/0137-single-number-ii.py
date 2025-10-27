class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num]+=1
            else:
                hmap[num] = 1
        for key, value in hmap.items():
            if value ==1:
                return key