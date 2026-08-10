class Solution:
    def dfs(self, node, cur_color, graph, color, visited):
        visited[node] = True
        color[node] = cur_color

        for nbr in graph[node]:
            if not visited[nbr]:
                if self.dfs(nbr, 1 - cur_color, graph, color, visited):
                    return True
            elif color[nbr] == color[node]:
                return True
        return False

    def isBipartite(self, graph):
        n = len(graph)
        color = [0] * n
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                if self.dfs(i, 0, graph, color, visited):
                    return False
        return True