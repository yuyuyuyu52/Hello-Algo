from graph_adjacency_list import GraphAdjacencyList
def dfs(graph:GraphAdjacencyList, start_vertex, visited,res:list):
    visited.add(start_vertex)
    res.append(start_vertex)
    for vertex in graph.adj_list[start_vertex]:
        if vertex not in visited:
            dfs(graph, vertex, visited,res)

# 列表，字典，集合，元组
# 集合具有无序性，因此它们的输出顺序可能不同于输入顺序。

if __name__ == '__main__':
    g=GraphAdjacencyList()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,5)
    g.add_edge(3,0)
    g.add_edge(4,5)
    g.add_edge(5,6)
    visited = set()
    res=[]
    dfs(g,0,visited,res)
    print(res)

