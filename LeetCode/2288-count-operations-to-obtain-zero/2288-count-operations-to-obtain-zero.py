class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count=0
        while num1 !=0 and num2 !=0:
            if num2 >= num1:
                num2-=num1
            else:
                num1-=num2
            count+=1
        return count

