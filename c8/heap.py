#分类: min heap-->parent<=child    max heap-->parent>=child
#数据结构:为了更好的存储数据和处理数据而生

# max heap的实现
class heap:
    # 建堆可以通过push来进行，但是效率有点低。
    def __init__(self):
        self.arr=[9,8,6,6,7,5,2,1,4,3,6,2]

    #建立连接
    def left(self,i:int):
        return i*2+1
    def right(self,i:int):
        return i*2+2
    def parent(self,i:int):
        return (i-1)//2


    def peek(self):
        return self.arr[0]

    def push(self,val:int):
        index=len(self.arr)
        self.arr.append(val)
        self.siftup(index)


    def pop(self):
        poped_num=self.arr[0]
        self.arr[0]=self.arr[-1]
        self.arr.pop()

        index=0
        while self.arr[index]<self.arr[self.left(index)] or self.arr[index]<self.arr[self.right(index)]:
            pass
        return poped_num

    # 从i开始向下堆化
    def siftdown(self,i:int):
        flag=1
        while flag:
            if self.arr[(self.left(i))] and self.arr[self.right(i)]:

                if val==self.arr[self.right(i)]:
                    self.arr[self.right(i)]=self.arr[i]
                    i=self.right(i)

                else:
                    self.arr[self.left(i)]=self.arr[i]
                    i=self.left(i)

                self.arr[i]=val

            else:
                val=self.arr[(self.left(i))] or self.arr[self.right(i)]
                # if

                self.arr[i]




    #从i开始向上堆化
    def siftup(self,index:int):
        while self.arr[self.parent(index)]<self.arr[index]:
            # 交换两个变量数据a,b=b,a
            self.arr[index],self.arr[self.parent(index)]=self.arr[self.parent(index)],self.arr[index]
            index=self.parent(index)

if __name__ == '__main__':
    h1=heap()
    print(h1.arr)
    h1.push(7)
    print(h1.arr)


