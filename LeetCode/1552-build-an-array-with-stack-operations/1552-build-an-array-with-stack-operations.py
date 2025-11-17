class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        arr=[]
        ans = []
        for i in range(1,n+1):
            arr.append(i)
        iter=0
        for i in range(len(arr)):
            if iter == len(target):
                return ans
            if arr[i] == target[iter]:
                ans.append("Push")
                iter+=1
                continue
            else:
                ans.append("Push")
                ans.append("Pop")




        return ans
            