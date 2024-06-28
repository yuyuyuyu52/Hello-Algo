

class MyList:

    def __init__(self):
        self.capacity:int=10
        self.size:int=0
        self.extend_ratio=2
        self.arr:list[int]=[0]*self.capacity

    def get(self,index:int):
        if 0<=index<self.capacity:
            return self.arr[index]
        return

    def set(self,index:int,num:int):
        if 0<=index<self.capacity:
            self.arr[index]=num


    def extend(self):
        if self.capacity == self.size:
            self.capacity=self.capacity*self.extend_ratio
            self.new_arr:list[int]=[0]*self.capacity
            for i in range(len(self.arr)):
                self.new_arr[i]=self.arr[i]
            self.arr=self.new_arr


    def add(self,num:int):
        self.extend()
        self.arr[self.size]=num
        self.size+=1


    def remove(self,index:int):
        if  not 0<=index<self.size:
            raise IndexError
        for i in range(index,len(self.arr)-1):
            self.arr[i]=self.arr[i+1]
        self.size-=1

    # extend the list before inserting  an element
    def insert(self,index:int,num:int):
        self.extend()
        for i in range(self.size,index,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[index]=num
        self.size+=1

    # show the valid elements
    def to_arr(self):
        print(self.arr[:self.size])



a=MyList()

for i in range(100):
    a.add(i)
a.insert(1,100)
a.to_arr()
