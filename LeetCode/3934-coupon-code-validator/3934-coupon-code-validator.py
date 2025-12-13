class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        ans = []
        res = []
        for i in range(len(code)):
            if (code[i].isalnum() or "_" in code[i]) and code[i] != " "and businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"] and isActive[i] == True:
                ans.append((code[i], businessLine[i]))
        ans = sorted(ans,key =lambda x: (x[1], x[0]))
        for a in ans:
            res.append(a[0])
        return res
            
        