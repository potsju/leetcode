class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)-k+1):
            c = Counter(nums[i:i+k])
            c = sorted(c.items(), key = lambda x: (x[1], x[0]), reverse= True)
            sum=0
            for j in range(min(x,len(c))):
                sum += c[j][1] * c[j][0]
            arr.append(sum)
        return arr

            