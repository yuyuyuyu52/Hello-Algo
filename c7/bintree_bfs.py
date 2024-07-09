from bin_tree import BinTreeNode,n1

from collections  import deque

def level_order(root:BinTreeNode):
    if root is None:
        return
    que=deque()
    res=[]
    que.append(root)

    while que:
        node:BinTreeNode=que.popleft()
        res.append(node.val)
        if node.nextleft is not None:
            que.append(node.nextleft)
        if node.nextright is not None:
            que.append(node.nextright)
    return res

res=[]

def pre_order(root:BinTreeNode):
    if root is None:
        return

    res.append(root.val)
    pre_order(root.nextleft)
    pre_order(root.nextright)

def in_order(root:BinTreeNode):
    if root is None:
        return
    in_order(root.nextleft)
    res.append(root.val)
    in_order((root.nextright))

def last_order(root:BinTreeNode):
    if root is None:
        return
    last_order(root.nextleft)
    last_order(root.nextright)
    res.append(root.val)

if __name__ == '__main__':
    last_order(n1)
    print(res)
