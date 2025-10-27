class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        while num * num <= x:
            if num*num == x:
                return num
            if (num+1) * (num+1) > x:
                return num
    
            else:
                num+=1
            
        return num