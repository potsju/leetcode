class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap = {}
        for key,value in enumerate(nums):
            if value not in hmap:
                hmap[value] = [key]
            else:
                hmap[value].append(key)
        dist = float('inf')
        for key,value in hmap.items():
            if len(value) >=3:
                for i in range(2,len(value)):
                    sum=0
                    sum += abs(value[i] - value[i-1]) + abs(value[i]-value[i-2]) + abs(value[i-1]- value[i-2])
                    dist= min(sum, dist)
        return -1 if dist == float('inf') else dist