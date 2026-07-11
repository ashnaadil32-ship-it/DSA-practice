from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [False] * n
        complete_components = 0
        
        def dfs(node):
            visited[node] = True
            nodes = 1
            # Total degree contribution of this specific node
            edges_count = len(graph[node])
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    n_count, e_count = dfs(neighbor)
                    nodes += n_count
                    edges_count += e_count
                    
            return nodes, edges_count

        for i in range(n):
            if not visited[i]:
                # Find total nodes and sum of degrees for the component
                node_count, total_edges = dfs(i)
                
                # Check if it forms a complete graph component
                if total_edges == node_count * (node_count - 1):
                    complete_components += 1
                    
        return complete_components