import numpy as np

class GraphAdjacencyMatrix:
    def __init__(self,vertices:list[int],edges:list[list[int]]):
        # 顶点
        self.vertices = vertices
        # 边
        self.adjacency_matrix:list[list[int]]=edges


    def size(self):
        return len(self.vertices)

    def add_vertex(self,val:int):
        self.vertices.append(val)
        n=self.size()
        for i in self.adjacency_matrix:
            i.append(0)
        self.adjacency_matrix.append([0]*n)


    def get_index(self,val:int):
        index=0
        for i in self.vertices:
            if val==i:
                return index
            else:
                index+=1
        return

    def remove_vertex(self,val:int):
        i=self.get_index(val)
        self.vertices.remove(val)
        del self.adjacency_matrix[i]
        for x in self.adjacency_matrix:
            del x[i]

    def add_edge(self,val1:int,val2:int):
        i=self.get_index(val1)
        j=self.get_index(val2)
        if not i and j:
            return

        self.adjacency_matrix[i][j] = 1
        self.adjacency_matrix[j][i] = 1

    def remove_edge(self,val1:int,val2:int):
        i=self.get_index(val1)
        j=self.get_index(val2)
        if not i and j:
            return
        self.adjacency_matrix[j][i]=0
        self.adjacency_matrix[i][j] = 0
    def show_graph(self):
        print(self.vertices)
        print(np.array(self.adjacency_matrix))

if __name__ == '__main__':
    g=GraphAdjacencyMatrix([2,3],[[0,1],
                                                [1,0]])
    g.add_vertex(1)
    g.add_vertex(8)
    g.add_edge(1,8)
    g.remove_vertex(2)
    g.remove_edge(1,8)
    g.show_graph()

'''
[2, 3, 1, 8]
[[0 1 0 0]
 [1 0 0 0]
 [0 0 0 1]
 [0 0 1 0]]
'''