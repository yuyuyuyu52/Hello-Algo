stack:list[int]=[]

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# get the top element but not get it out
peek:int=stack[-1]

# get the top element and get it out
pop:int=stack.pop()

size:int=len(stack)

is_empty:bool=len(stack)==0

from c4.linked_list import ListNode


# 在类中,成员函数和成员不能有重名
class LinkedListStack:
    def __init__(self):
        self.top: ListNode | None=None
        self._size:int=0

    def push(self,num:int):
        if not self.top:
            self.top=ListNode(num)
        else:
            new_peek=ListNode(num)
            new_peek.next=self.top
            self.top=new_peek
        self._size+=1


    def peek(self):
        return self.top.num

    def pop(self):
        top=self.top
        self.top=self.top.next
        self._size-=1
        return top.num

    def size(self):
        return self._size


if __name__ == '__main__':

    stack1=LinkedListStack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    aa=stack1.pop()
    print(aa)
    print(stack1.peek())
    print(stack1.size())

