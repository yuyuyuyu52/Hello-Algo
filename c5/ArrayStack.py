class ArratStack:
    def __init__(self):
        self.arr=[]

    def push(self,num:int):
        self.arr.append(num)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[-1]

    def size(self):
        return len(self.arr)

if __name__ == '__main__':
    ss=ArratStack()
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)

    print(ss.pop())
    print(ss.peek())
    print(ss.size())