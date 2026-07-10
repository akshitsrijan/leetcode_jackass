class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        '''res=[]
        for i in range(len(temperatures)):
            c=0
            for j in range(i+1,len(temperatures)):
                if i== len(temperatures)-1:
                    c = 0
                    break
                c = c+1
                if temperatures[j]>temperatures[i]:
                    res.append(c)
                    break
                else:
                    res.append(0)
           
        return res'''
        res = [0] * len(temperatures)
        stack = []
       
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
               prev = stack.pop()
               res[prev] = i - prev
            stack.append(i)

        return res

        
                
                
        