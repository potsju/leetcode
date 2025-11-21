class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        left= {}
        right ={}
        for i, ch in enumerate(s):
            if ch not in left:
                left[ch] = i
        for i in range(len(s)-1,-1,-1):
            ch = s[i]
            if ch not in right:
                right[ch] = i
                           
        res = 0
        for ch in left:
            if left[ch] < right[ch]:
                mid_chars= set(s[left[ch]+1 : right[ch]])
                res += len(mid_chars)
        return res
