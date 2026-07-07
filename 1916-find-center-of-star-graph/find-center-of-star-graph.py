class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        e1,e2=edges[:2]
        for i in e1:
            if i in e2:
                return i
               
                

                    
