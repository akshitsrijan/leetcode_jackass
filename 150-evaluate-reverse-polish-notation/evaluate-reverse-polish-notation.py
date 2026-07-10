class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res=[]
        for i in tokens:
            if i=="+":
                s=int(res[-2])+int(res[-1])
                res.pop()
                res.pop()
                res.append(s)
            elif i=="-":
                diff=int(res[-2])-int(res[-1])
                res.pop()
                res.pop()
                res.append(diff)
            elif i=="*":
                prod=int(res[-2])*int(res[-1])
                res.pop()
                res.pop()
                res.append(prod)
            elif i == "/":
                
                num2 = res.pop()
                num1 = res.pop()
                div = int(float(num1)/float(num2))
                res.append(div)

            else:
                res.append(int(i))
        return res[0]
        