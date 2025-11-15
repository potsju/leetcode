class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        count = [1] + [0] * (n + n + 2)
        acc = [1] + [0] * (n + n + 2)
        res = pre = 0
        for n in nums:
            if n == target:
                pre+=1
            else:
                pre -=1
            count[pre]+=1
            acc[pre] = acc[pre - 1] + count[pre]
            res += acc[pre - 1]
        return res