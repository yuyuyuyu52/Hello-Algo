class ListNode:
    def __init__(self,num:int):
        self.num:int=num
        self.next:ListNode|None=None
        self.prev:ListNode|None=None


class LinkedListDeque:
    def __init__(self):
        self._size:int=0
        self.front_node:ListNode|None=None
        self.rear_node:ListNode|None=None

    def popleft(self):
        if not self._size==0:
            num=self.front_node.num
            self.front_node=self.front_node.next
            self._size-=1
            return num


    def popright(self):
        if not self._size == 0:
            num=self.rear_node.num
            self.rear_node=self.rear_node.prev
            self._size -= 1
            return num

    def pushright(self,num:int):
        node=ListNode(num)
        if self._size==0:
            self.front_node=self.rear_node=node
        else:
            self.rear_node.next=node
            node.prev=self.rear_node
            self.rear_node=node
        self._size+=1

    def pushleft(self,num:int):
        node = ListNode(num)
        if self._size == 0:
            self.front_node = self.rear_node = node
        else:
            node.next = self.front_node
            self.front_node.prev=node
            self.front_node = node
        self._size += 1


    def to_arr(self):
        arr=[]
        arr.append(self.front_node.num)
        node=self.front_node
        for i in range(self._size-1):
            node=node.next
            arr.append(node.num)
        return arr



    def size(self):
        return self._size




if __name__ == '__main__':
    LLD=LinkedListDeque()
    LLD.pushright(0)
    LLD.pushright(1)
    LLD.pushright(2)

    LLD.pushright(3)

    LLD.pushleft(-1)
    LLD.pushleft(-2)
    LLD.pushleft(-3)
    LLD.pushleft(-4)
    print(LLD.popright())
    print(LLD.size())
    print(LLD.to_arr())
