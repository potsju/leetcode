class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findleft():
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return left
        def findright():
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] <= target:
                    left= mid+1
                else:
                    right =mid-1
            return right
        left= findleft()
        right = findright()
        if left < len(nums) and right >=0 and nums[right] == target and nums[left] == target:
            return [left,right]
        else:
            return [-1,-1]