class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        iter= 0
        sum = 0
        while iter < len(digits):
            sum += int(digits[iter]) * pow(10, len(digits)-iter-1)
            iter+=1
        sum+=1
        sum = str(sum)
        l = []
        for i in range(len(sum)):
            l.append(int(sum[i]))
        return l
       