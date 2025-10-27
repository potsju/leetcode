class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        iter = n
        while n > 1:
            iter *= n-1
            n-=1
        x = list(str(iter))
    
        sum =0
        for i in range(len(x)-1,-1,-1):
            if x[i] == '0':
                print("hello")
                sum+=1
            elif x[i] != '0':
                return sum
        return 0
        