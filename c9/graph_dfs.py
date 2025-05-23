from graph_adjacency_list import GraphAdjacencyList
"""
graph_dfs.py
本文件实现了基于邻接表的图的深度优先搜索（DFS）算法。
主要内容：
- 导入 GraphAdjacencyList 类，用于表示图的邻接表结构。
- 实现 dfs 函数，递归遍历图中的所有可达节点。
- 在主程序中，构建一个简单的无向图，并演示 DFS 的使用方法。
函数说明：
dfs(graph: GraphAdjacencyList, start_vertex, visited, res: list)
    对给定图从指定起点进行深度优先遍历。
    参数：
        graph: GraphAdjacencyList 图的邻接表表示
        start_vertex: 遍历起点
        visited: 已访问节点的集合
        res: 遍历结果列表
注意事项：
- 集合（set）是无序的，因此遍历顺序可能与输入顺序不同。
"""

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

