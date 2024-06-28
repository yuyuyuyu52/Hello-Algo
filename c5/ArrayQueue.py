class ArrayQueue1:
    def __init__(self):
        self.arr=[]

    def push(self,num:int):
        self.arr.append(num)

    def pop(self):
        num=self.arr[0]
        self.arr=self.arr[1:]
        return num

    def peek(self):
        return self.arr[0]

    def size(self):
        return len(self.arr)

class ArrayQueue:
    def __init__(self,size):
        self.arr:list[int]=[0]*size
        self._size:int=0
        self.front:int=0

    def push(self,num:int):
        if self._size<len(self.arr):
            self.arr[((self._size+self.front)%len(self.arr))]=num
            self._size+=1
    def pop(self):
        num=self.arr[self.front]
        self.front=(self.front+1)%len(self.arr)
        self._size-=1
        return num
    def peek(self):
        return self.arr[self.front]

    def size(self):
        return self._size

    def to_arr(self):
        res=[]
        for i in range(self._size):
            res.append(self.arr[(self.front+i)%len(self.arr)])
        return res


if __name__ == '__main__':
    aa=ArrayQueue(10)
    for i in range(10):
        aa.push(i)
    aa.pop()
    aa.push(10)
    aa.pop()
    aa.pop()
    for i in range(8):
        aa.pop()
    print(aa.to_arr())

