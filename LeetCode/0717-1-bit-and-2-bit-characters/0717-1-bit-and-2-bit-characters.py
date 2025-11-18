class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        last = True
        stack =[]
        for b in bits:
            if b == 1 and not stack:
                last = False
                stack.append(b)
            elif len(stack) ==1 and (stack[-1] == 0 or stack[-1] == 1) and (b ==0 or b== 1):
                last = False
                stack.pop()
                continue
            elif b== 0 and not stack:
                last = True
                continue
        return last