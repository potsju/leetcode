class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = sorted(Counter(nums).items(), key= lambda x: x[0])
        right = len(count)
        ans =0
        prefix = [0] * (len(count))
        prefix[-1] =count[-1][1]
        for i in range(len(count)-2,-1,-1):
            prefix[i] = prefix[i+1] + count[i][1]
        
        if k==0:
            return len(nums)
        if len(count)==1:
            return 0
        for i in range(len(count)):
            greater = prefix[i]- count[i][1]
            if greater >= k:
                ans+=count[i][1]
        return ans

            