class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def contains_all_elements(hmap3,hmap4):
            for key,value in hmap4.items():
                if key not in hmap3 or hmap3[key] < value:
                    return False
            return True
        hmap1 = Counter(t)
        hmap2 = {}
        left=0
        minlen = float('inf')
        ans = ""
        for right in range(len(s)):
            if s[right] not in hmap2:
                hmap2[s[right]] =1
            else:
                hmap2[s[right]]+=1
            while contains_all_elements(hmap2, hmap1):
                if right-left+1 < minlen:
                    ans = s[left:right+1]
                    minlen = right-left+1
                if s[left] in hmap2:
                    hmap2[s[left]]-=1 
                    if hmap2[s[left]] ==0:
                        del hmap2[s[left]]
                left+=1
        return ans if ans else ""



            