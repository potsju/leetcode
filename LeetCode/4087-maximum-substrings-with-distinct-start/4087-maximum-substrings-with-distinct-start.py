class Solution:
    def maxDistinct(self, s: str) -> int:
        start = set()
        ans =0
        for letter in s:
            if letter not in start:
                start.add(letter)
                ans+=1
        return ans
