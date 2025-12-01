class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        res = inf
        pre = {}
        for i, a in enumerate(nums):
            if a in pre:
                res = min(res,i-pre[a])
            pre[int(str(a)[::-1])] = i
        return res if res < inf else -1