class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        arr = []
        for row in matrix:
            arr.extend(row)
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if target == arr[mid]:
                return True
            if target> arr[mid]:
                left = mid+1
            elif target < arr[mid]:
                right = mid-1
        return False
            

                