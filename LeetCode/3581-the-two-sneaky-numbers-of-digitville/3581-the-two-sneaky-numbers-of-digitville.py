class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = Counter(nums)
        arr=[]
        for key,value in c.items():
            if value == 2:
                arr.append(key)
        return arr