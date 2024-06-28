class BinTreeNode:
    def __init__(self,val:int):
        self.nextleft:None|BinTreeNode=None
        self.nextright:None|BinTreeNode=None
        self.val=val

n1=BinTreeNode(1)
n2=BinTreeNode(2)
n3=BinTreeNode(3)
n4=BinTreeNode(4)
n5=BinTreeNode(5)

n1.nextleft=n2
n1.nextright=n3
n2.nextleft=n4
n2.nextright=n5


if __name__ == '__main__':
    print(n5.nextleft)