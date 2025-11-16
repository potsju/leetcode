class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr= []
        nums.sort()
        arr2= []
        for i in range(1,len(nums)+1):
            arr2.append(i)
        s = dict(Counter(nums))
        for key,value in s.items():
            if value == 2:
                ans1= key
        arr.append(ans1)
        ans2=0
        for i in range(len(nums)):
            if arr2[i] not in nums:
                ans2 = arr2[i]
                break
        arr.append(ans2)
        return arr


        
