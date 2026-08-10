
class Solution:
    def networkDelayTime(self, times, n,k):
        # 1. Build adjacency list using 1-based indexing (size n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
            
        # 2. Initialize distances with infinity (size n + 1)
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        # 3. Priority queue stores tuples of (distance, node)
        pq = [(0, k)]
        
        while pq:
            wt, node = heapq.heappop(pq)
            
            # Skip if we found a shorter path to this node already
            if wt > dist[node]:
                continue
                
            # Relax neighboring edges
            for nbr, w in adj[node]:
                if wt + w < dist[nbr]:
                    dist[nbr] = wt + w
                    heapq.heappush(pq, (dist[nbr], nbr))
                    
        # 4. Find max distance ignoring the unused 0th index
        ans = max(dist[1:])
        
        return -1 if ans == float('inf') else ans