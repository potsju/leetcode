class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t != "/" and t != "*" and t != "+" and t != "-":
                stack.append(int(t))
            else:
                cur2 = stack.pop()
                cur1 = stack.pop()
                if t == "/":
                    stack.append(int(float(cur1) / cur2))
                elif t == "*":
                    stack.append(cur1 * cur2)
                elif t == "-":
                    stack.append(cur1 - cur2)
                elif t == "+":
                    stack.append(cur1 + cur2)
    
        return stack[0]
                    

                    

    
                    
