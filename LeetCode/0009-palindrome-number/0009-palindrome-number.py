class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
                continue
            else:
                return False
        return True