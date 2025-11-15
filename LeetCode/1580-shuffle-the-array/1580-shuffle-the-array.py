class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr1 = nums[:(n)]
        arr2 = nums[n:]
        arr = []
        iter=0
        while iter< n:
            arr.append(arr1[iter])
            arr.append(arr2[iter])
            iter+=1
        return arr