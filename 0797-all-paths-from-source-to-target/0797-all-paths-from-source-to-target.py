class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        result = []
        
        def dfs(node, path):
            
            if node == target:
                result.append(list(path))
                return
            
            
            for neighbor in graph[node]:
                path.append(neighbor)     
                dfs(neighbor, path)       
                path.pop()                
        dfs(0, [0])
        return result