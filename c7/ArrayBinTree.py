# 当可变对象作为参数传给函数时,函数会使用该函数的引用而非复制,因此在函数内改变此对象,会对全局对象造成影响,可用list(arr)解决
class ArrayBinTree:
    def __init__(self,arr:list[int|None]):
        self._tree=list(arr)
        self.res=[]

    #get the index node value
    def val(self,index:int):
        if index<0 or index>len(self._tree)-1:
            return None
        else:
            return self._tree[index]

    # get the left node of the index node
    def left(self,index:int):
        return 2*index+1

    # get the right node of the index node
    def right(self,index:int):
        return 2*index+2

    # get the parent node index
    def parent(self,index:int):
        return (index-1)//2

    def level_order(self):
        self.res=[]
        for i in self._tree:
            if i is not None:
                self.res.append(i)

        return self.res

    def dfs(self,order:int):
        self.res=[]
        # 1->pre,2->in,3->post
        if order==1:
            self.pre_order()
            return self.res
        elif order==2:
            self.in_order()
            return self.res
        elif order==3:
            self.post_order()
            return self.res

    def pre_order(self,index:int=0):
        if self.val(index)==None:
            return None

        self.res.append(self._tree[index])
        self.pre_order(self.left(index))
        self.pre_order(self.right(index))

    def post_order(self,index:int=0):
        if self.val(index) == None:
            return None
        self.post_order(self.left(index))
        self.post_order(self.right(index))
        self.res.append(self._tree[index])


    def in_order(self,index:int=0):
        if self.val(index) == None:
            return None
        self.in_order(self.left(index))
        self.res.append(self._tree[index])
        self.in_order(self.right(index))



# 对于pre-order,in-order,post-order有了一个大致了解，就是把所有节点都简化成只有三个节点，即母节点，和他的左节点和右节点，永远只往下看
# pre-order就是母左右,in-order就是左母右,post-order就是左右母

if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,None,9,10]
    bt=ArrayBinTree(arr)
    print(bt.level_order())

    print(bt.dfs(3))




