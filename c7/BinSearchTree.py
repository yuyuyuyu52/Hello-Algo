from bin_tree import BinTreeNode

#build a binary search tree
# 1-10
n1=BinTreeNode(1)
n2=BinTreeNode(2)
n3=BinTreeNode(3)
n4=BinTreeNode(4)
n5=BinTreeNode(5)
n6=BinTreeNode(6)
n7=BinTreeNode(7)
n8=BinTreeNode(8)
n9=BinTreeNode(9)
n10=BinTreeNode(10)
n2.nextleft=n1
n2.nextright=n3


class BinarySearchTree:
    def __init__(self, root:BinTreeNode):
        self.root=root

    def search(self, target:int):
        pre:BinTreeNode|None=None
        current = self.root
        while current:
            if current.val == target:
                break

            elif current.val < target:
                pre=current
                current = current.nextright

            else:
                pre=current
                current = current.nextleft




        # print(current,pre.val)
        if current is None:
            return pre
        return current

    def insert(self, target:int):
        if self.root == None:
            self.root = BinTreeNode(target)

        else:
            # node = self.search(
            pass


bt=BinarySearchTree(n2)
print(bt.search(1).val)