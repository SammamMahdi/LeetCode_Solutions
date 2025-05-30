class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = bfs(edges, node1, n)
        print(dist1)
        dist2 = bfs(edges, node2, n)
        print(dist2)
        min_dist = float("inf")
        curr_node = -1
        for i in range(len(edges)):
            if dist1[i] is not None and dist2[i] is not None:
                curr_dist = max(dist1[i], dist2[i])
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    curr_node = i
        return curr_node


def bfs(edges, node, n):
    queue = [node]
    dist = [None] * n
    dist[node] = 0
    while queue:
        curr_node = queue.pop(0)
        if edges[curr_node] != -1:
            if dist[edges[curr_node]] is None:
                dist[edges[curr_node]] = dist[curr_node] + 1
                queue.append(edges[curr_node])
    return dist


edges = [9, 8, 7, 0, 5, 6, 1, 3, 2, 2]
node1 = 1
node2 = 6
print(Solution().closestMeetingNode(edges, node1, node2))
