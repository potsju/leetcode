class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans =0
        cur =1
        prevcur = 1
        for i in range(0,n):
            ans +=cur
            cur +=1
            if (i+1)% 7 == 0 and i != 0:
                prevcur +=1
                cur = prevcur
                continue
           
        return ans