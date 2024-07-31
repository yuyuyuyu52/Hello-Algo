# 顶点类
class Vertex:
    def __init__(self, value):
        self.val=value

class GraphAdjacencyList:
    def __init__(self):
        self.adj_list:dict[Vertex,list[Vertex]]={}


    def size(self):
        return len(self.adj_list)


    def add_edge(self, vertex1, vertex2):
        if not vertex1 in self.adj_list and vertex2 in self.adj_list:
            return
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)


    def add_vertex(self, vertex):
        if vertex in self.adj_list:
            return
        self.adj_list[vertex]=[]


    def remove_vertex(self, vertex):
        del self.adj_list[vertex]
        for i in self.adj_list.items():
            if vertex in i[1]:
                i[1].remove(vertex)


    def remove_edge(self, vertex1, vertex2):
        if not vertex1 in self.adj_list[vertex2] and vertex2 in self.adj_list[vertex1]:
            return
        self.adj_list[vertex1].remove(vertex2)
        self.adj_list[vertex2].remove(vertex1)


    def show_graph(self):
        for i in self.adj_list.items():
            print(i)


if __name__ == '__main__':
    g=GraphAdjacencyList()
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.remove_vertex(4)
    g.remove_edge(2,3)
    g.show_graph()