class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hmap= {}
        for num in nums:
            hmap[num]=1
        res = []
        for num in range(1,len(nums)+1):
            if num not in hmap:
                res.append(num)
        return res