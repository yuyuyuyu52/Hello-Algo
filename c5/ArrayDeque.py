class ArrayDeque:
    def __init__(self,num:int):
        self.arr:list[int]=[0]*num
        self._size:int=0
        self.front:int=0

    def pushright(self,num:int):
        if self._size<len(self.arr):
            self.arr[(self.front+self._size)%len(self.arr)]=num
            self._size+=1

    def pushleft(self,num:int):
        if self._size<len(self.arr):
            self.front=(self.front-1)%len(self.arr)
            self.arr[self.front]=num
            self._size+=1

    def popright(self):
        if self._size>0:
            num=self.arr[(self._size+self.front-1)%len(self.arr)]
            self._size-=1
            return num

    def popleft(self):
        if self._size > 0:
            num = self.arr[self.front]
            self.front=(self.front+1)%len(self.arr)
            self._size -= 1
            return num

    def size(self):
        return self._size

    def peekright(self):
        if self._size>0:
            return self.arr[(self.front+self._size-1)%len(self.arr)]

    def peekleft(self):
        if self._size > 0:
            return self.arr[self.front]


    def to_arr(self):
        arr=[]
        for i in range(self._size):
            arr.append(self.arr[(self.front+i)%len(self.arr)])
        return arr




if __name__ == '__main__':
    ad=ArrayDeque(10)
    for i in range(9):
        ad.pushright(i)
    ad.popright()
    ad.popright()
    for i in range(-1,-4,-1):
        ad.pushleft(i)

    ad.popleft()
    ad.popleft()

    print(ad.peekleft())
    print(ad.peekright())

    print(ad.to_arr())
    print(ad.popright())