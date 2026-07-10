class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """



    
        
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
            
        for char in s:
            if char in mapping:  # it's a closing bracket
                    # check if stack is empty or top doesn't match
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:  # it's an opening bracket
                stack.append(char)
            
            # valid only if stack is empty at the end
        return not stack

                    

        


       
           