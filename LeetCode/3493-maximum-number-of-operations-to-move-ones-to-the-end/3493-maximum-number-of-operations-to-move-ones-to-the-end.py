class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        ones =0
        use= False
        for c in s:
            if c == "0":
                use = True
            elif c== "1":
                if use == True:
                    res+=ones
                ones+=1
                use = False
        if use:
            res+=ones
        return res