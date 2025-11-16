class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        right =0
        cur =0
        while right < len(s):
            if s[right] == "1":
                cur+=1
                right+=1
                continue
            else:
                total += (cur * (cur+1)) // 2
                cur = 0
            right+=1
        if cur:
            total += (cur * (cur+1))//2
        return total %(pow(10,9) + 7)

            
