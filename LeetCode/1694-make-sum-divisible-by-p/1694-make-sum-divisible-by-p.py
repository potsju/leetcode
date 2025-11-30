class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0 :
            return 0
        hmap = {0 :- 1}
        prefix= 0
        res = len(nums)
        for i,x in enumerate(nums):
            prefix = (prefix + x) % p
            need = (prefix-target) % p
            if need in hmap:
                res = min(res,i-hmap[need])
            hmap[prefix] = i
        if res == len(nums):
            return -1
        else:
            return res