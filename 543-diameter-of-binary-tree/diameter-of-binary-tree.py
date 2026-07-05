# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        '''self.diameter=0
        def diameter(node):
            if not node:
                return 0
                left=diameter(node.left)
                right=diameter(node.right)
            self.diameter=max(self.diameter,left+right)
            return 1+max(left,right)
        diameter(root)
        return self.diameter'''
       
        
            
        self.d=0
        
        def dfs(self,node):
            if not node:
                return 0
                
            right=dfs(self,node.right)
            left=dfs(self,node.left)
            self.d = max(self.d,left + right)
            return max(left,right)+1
        dfs(self,root)
        return self.d

        