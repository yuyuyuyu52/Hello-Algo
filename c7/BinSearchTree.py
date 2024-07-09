from bin_tree import BinTreeNode
from bintree_bfs import level_order,res
#build a binary search tree
n2=BinTreeNode(2)
n2.nextleft=BinTreeNode(1)
n2.nextright=BinTreeNode(3)

def in_order(root:BinTreeNode):
    if root == None:
        return
    in_order(root.nextleft)
    res.append(root)
    in_order(root.nextright)

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


        return pre,current

    # def insert(self, target:int):
    #     if self.root == None:
    #         self.root = BinTreeNode(target)
    #
    #     else:
    #         if self.search(target)[-1].val==target:
    #             print('error,the num has been exist')
    #         elif self.search(target).val<target:
    #             self.search(target).nextright=BinTreeNode(target)
    #         else:
    #             self.search(target).nextleft=BinTreeNode(target)


    def insert2(self, target:int):
        if self.root == None:
            self.root = BinTreeNode(target)
        else:
            if self.search(target)[-1] is None:
                if self.search(target)[0].val>target:
                    self.search(target)[0].nextleft=BinTreeNode(target)
                else:
                    self.search(target)[0].nextright=BinTreeNode(target)
            else:
                print('error,the num has been exist')


    # in-order can find the smallest node from the root node to ye node
    # pre-order  can find the biggest node
    # delete a node is set the next node of parent node to be None
    def remove(self, target:int):
         # 怎么判断一个节点是他父节点的哪个节点
        def du(node:BinTreeNode):
            du=0
            if node.nextleft is not None:
                du+=1
            if node.nextright is not None:
                du+=1
            return du

        current=self.search(target)[-1]
        parent=self.search(target)[0]

        # is the removing num exist?
        if current is None:
            print('the num is not exist')
            return

        if current.val==target:
            du=du(current)


            # 0
            # if du==0:
            #     if parent.val>target:
            #         parent.nextleft=None
            #     else:
            #         parent.nextright=None

            # 1
            if  du==1 or du==0:
                child=current.nextright or current.nextleft
                if parent.nextleft==current:
                    parent.nextleft=child
                else:
                    parent.nextright=child


                '''old method:confused'''
                # if current.nextright is None:
                #     if parent.nextleft.val==current.val:
                #         parent.nextleft=current.nextleft
                #     else:
                #         parent.nextright=current.nextleft
                # else:
                #     if parent.nextleft.val == current.val:
                #         parent.nextleft = current.nextright
                #     else:
                #         parent.nextright = current.nextright


            # 2
            elif du==2:
                # get the right node(smallest of rightnext, biggest of the leftnext) choose the rightnext use in-order
                in_order(current.nextright)
                target_node=res[0]
                # delete the target node
                num=target_node.val
                self.remove(num)
                # set the first node to the target node
                current.val=num








if __name__ == '__main__':

    bt=BinarySearchTree(n2)
    bt.insert2(4)
    bt.insert2(5)
    # print(n2.nextright.nextright.val)
    # bt.insert(0)
    bt.insert2(10)
    bt.insert2(9)
    bt.insert2(11)
    print(level_order(n2))
    bt.remove(10)
    print(level_order(n2))
    # print(bt.search(4)[0].val,bt.search(4)[-1])








    # ???
    n3=BinTreeNode(6)
    n2=None
    a=n3 or n2
    print(a.val)


# 在 Python 中，假值包括以下几种：
# None：空值。
# False：布尔值 False。
# 数字 0：包括整数 0、浮点数 0.0、复数 0j 等。
# 空序列：包括空字符串 ''、空列表 []、空元组 () 等。
# 空集合：包括空集合 set()、空字典 {} 等。
# 空范围对象：range(0)。
# 这些值在条件判断中会被解释为假值（即布尔值 False）


# and or
# 都遵从 从头到尾的原则，且懒惰
# a=n1 or n2
# 如果n1为真值则直接忽略n2，反之则直接为n2的值
# a=n1 and n2
# 若n1假则为n1，n1真则为n2