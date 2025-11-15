class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans=0
        for i in range(len(nums)):
            count =0
            total = 0
            for j in range(i,len(nums)):
                if nums[j] == target:
                    count+=1
                total+=1
                if count > total//2:
                    ans+=1
        return ans
        

                