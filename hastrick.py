class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=[]
        stack=[]
        for i in range(len(s)):
            l1.append(s[i])
        for i in l1:
            if i=='*':
                stack.pop()
            else:
                stack.append(i)
                
        return ''.join(stack)
       
