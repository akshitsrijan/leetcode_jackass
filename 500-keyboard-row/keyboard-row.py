class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1= "qwertyuiop"
        r2= "asdfghjkl"
        r3= "zxcvbnm"

        
        result=[]

        for w in words:
            c1,c2,c3=0,0,0
            for l in w:
                if l.lower() in r1:
                    c1 = c1+1
                if l.lower() in r2:
                    c2 = c2+1
                
                if l.lower() in r3:
                    c3 = c3+1
            if (c1!=0 and c2==0 and c3==0) or (c2!=0 and c1==0 and c3==0) or (c3!=0 and c2==0 and c1==0):
                result.append(w)
        return result