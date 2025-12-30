class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for t in tokens:
            if t in "+-*/" and len(t) == 1: 
                b, a = stk.pop(), stk.pop()
                
                if t == '+':
                    stk.append(a + b)
                elif t == '-':
                    stk.append(a - b)
                elif t == '*':
                    stk.append(a * b)
                else:
                    
                    stk.append(int(float(a) / b))
            else:
                stk.append(int(t))
                
        return stk[0]