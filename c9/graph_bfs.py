from collections import deque

"""
graph_bfs.py
本文件实现了基于邻接表的无向图的广度优先搜索（BFS）算法。
主要内容：
- graph_bfs(graph, vertex): 对给定的图从指定顶点进行广度优先遍历，返回遍历顺序的顶点列表。
- 示例代码展示了如何创建图、添加顶点和边，并调用BFS算法。
函数说明:
def graph_bfs(graph: GraphAdjacencyList, vertex: int) -> list[int]:
"""

from graph_adjacency_list import GraphAdjacencyList

def graph_bfs(graph:GraphAdjacencyList,vertex:int):
    res=[]
    visited:set[Vertex] ={vertex}
    # deque()需要一个可迭代对象作为参数,所以vertex不行,[vertex]才行
    que:deque[Vertex] = deque([vertex])

    while que:
        vertex = que.popleft()
        res.append(vertex)
        for i in graph.adj_list[vertex]:
            if i not in visited:
                visited.add(i)
                que.append(i)

    return res



if __name__ == '__main__':
    g=GraphAdjacencyList()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(4)
    g.add_vertex(3)
    g.add_edge(0,1)
    g.add_edge(0,3)
    g.add_edge(1,4)
    g.add_edge(3,4)
    print(graph_bfs(g,0))
