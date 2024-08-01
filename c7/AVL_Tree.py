class AVLNode:
    def __init__(self, val:int):
        self.val =val
        self.left :None|AVLNode= None
        self.right :None|AVLNode= None
        self.height:int = 0
'''
class AVLTree(BinarySearchTree):
    def insert2(self, target:int):
        super().insert2(target)#可以把父类的该方法加入，然后再添加额外的部分
        print(1)
'''

# AVLTree意为平衡二叉搜索树，即每一层节点都是满状态（除了叶节点）,特点在于旋转
class AVLTree:
    def __init__(self):
        self.root = None

    # 什么是height,叶节点的h是0,None是-1,根节点h最大
    def height(self,node:AVLNode|None) -> int:
        if node is None:
            return -1
        return self.height

    def update_height(self,node:AVLNode):
        node.height=max(self.height(node.left),self.height(node.right))+1

    #返回左子树的高度减去右子树的高度,所有节点的bf满足-1<=bf<=1
    def balance_factor(self,node:AVLNode|None) -> int:
        if node is None:
            return 0
        return self.height(node.left)-self.height(node.right)

    # 旋转，不会影响in-order遍历的结果
    # 解决失衡节点，应该从叶子往根看

    def right_rotate(self, node:AVLNode|None):
        child=node.left
        grandchild=child.right
        node.left=grandchild
        child.right=node
        self.update_height(child)
        self.update_height(node)
        return child

    def left_rotate(self, node:AVLNode|None):
        child = node.right
        grandchild = child.left
        node.right = grandchild
        child.left = node
        self.update_height(child)
        self.update_height(node)
        return child

    def left_right_rotate(self, node:AVLNode|None):
        child=node.left
        self.left_rotate(child)
        self.right_rotate(node)

    def right_left_rotate(self, node:AVLNode|None):
        child=node.right
        self.right_rotate(child)
        self.left_rotate(node)

    def rotate(self, node:AVLNode|None):
        factor_parent=self.balance_factor(node)
        if factor_parent>1:
            factor_child=self.balance_factor(node.left)
            if factor_child==1:
                self.right_rotate(node)
            elif factor_child==-1:
                self.left_right_rotate(node)


        elif factor_parent<-1:
            factor_child=self.balance_factor(node.right)
            if factor_child==1:
                self.right_left_rotate(node)
            elif factor_child==-1:
                self.left_rotate(node)


    # avl树的普通操作
    def insert(self, target:int,node=):

        if self.root is None:
            self.root = AVLNode(target)
        else:
            if target < self.root.val:







