def bfs(graph,start_node):
    visited=[]
    queue=[start_node]
    while queue:
 
        start_node=queue.pop(0)
        queue.append(graph[start_node])
        if start_node not in visited:
            visited+=[start_node]
    return(visited)




graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
print(bfs(graph, start_node))