"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        #hashmap: original note -> clone node

        visited = {}

        def dfs(node):

            #already cloned
            if node in visited:
                return visited[node]

            #create clone
            copy = Node(node.val)

            # store in hash map
            visited[node] = copy

            #clone neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
        
        return dfs(node)
        