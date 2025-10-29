class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c= Counter(nums)
        arr= []
        for key,value in c.items():
            if value == 1:
                arr.append(key)
        return arr