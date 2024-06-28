from collections import deque

que:deque[int]=deque()
que.append(1)
que.append(2)
que.append(3)
que.append(4)

a=que.pop()
a=que.popleft()

from c4.linked_list import ListNode

class LinkedListQueue:
    def __init__(self):
        self.head:ListNode|None=None
        self._size:int=0

    def push(self,num:int):
        if not self.head:
            self.head=ListNode(num)
            self._size+=1
        else:
            node=ListNode(num)
            current_node=self.head
            for i in range(self._size-1):
                current_node=current_node.next
            current_node.next=node
            self._size += 1



    def pop(self):
        num=self.head.num
        self.head=self.head.next
        self._size-=1
        return num

    def peek(self):
        return self.head.num

    def size(self):
        return self._size

    def to_arr(self):
        arr=[]
        node:ListNode|None=self.head
        arr.append(self.head.num)
        for i in range(self._size-1):
            node=node.next
            arr.append(node.num)

        return arr


if __name__ == '__main__':

    qq=LinkedListQueue()
    qq.push(1)
    qq.push(2)
    qq.push(3)
    qq.push(4)
    print(qq.peek())
    print(qq.pop())
    print(qq.size())
    print(qq.to_arr())
