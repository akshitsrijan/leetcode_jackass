from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
       
        

        visited = set()
        queue = deque([source])
        
        check=[]
        while queue:
            node=queue.popleft()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph[node]:
               if neighbor not in visited:
                queue.append(neighbor)
        return False
        



       
        

        
                
        