class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for edge in times:
            u, v, w = edge
            graph[u].append((w, v))
        parent = [None] * (n + 1)
        distance = [-1] * (n + 1)
        q = []
        heapq.heappush(q, (0, k))
        distance[k] = 0
        while q:
            d, u = heapq.heappop(q)
            for w, v in graph[u]:
                if distance[v] == -1 or distance[v] > d + w:
                    distance[v] = d + w
                    parent[v] = u
                    heapq.heappush(q, (d + w, v))
        return max(distance[1:]) if -1 not in distance[1:] else -1

        
        