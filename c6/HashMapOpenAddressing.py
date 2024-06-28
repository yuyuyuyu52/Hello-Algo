from ArrayHashMap import Pair
class HashMapOpenAddressing:
    def __init__(self):
        self._size:int=0
        self.capacity=10
        self.buckets:list[Pair|None]=[None]*self.capacity
        self.extend_retio=2
        self.load_thres=2/3
        self.TOMESTONE=Pair(-1,-1)

    def put(self,key:int,val:str):
        if self._size/self.capacity>=self.load_thres:
            self.extend()

        index=self.find(key)
        if self.buckets[index] not in [None,self.TOMESTONE]:
            self.buckets[index]=Pair(key,val)
        else:
            self.buckets[index]=Pair(key,val)
            self._size+=1



    def all_set(self):
        arr=[]
        for i in self.buckets:
            if i is not None:
                arr.append((i.key,i.val))
            else:
                arr.append(i)

        return arr


    def extend(self):
        self.capacity=self.capacity*self.extend_retio
        b=self.all_set()
        self.buckets=[None]*self.capacity
        self._size=0
        for i in b:
            if i is not None and i !=self.TOMESTONE:
                self.put(i[0],i[1])

    def hash_func(self,key:int):
        return key%self.capacity

    def find(self,key:int):
        t=-1
        index=self.hash_func(key)
        while 1:
            if self.buckets[index] is None:
                if t!=-1:
                    return t
                return index
            elif self.buckets[index].key==key:
                if t!=-1:
                    self.buckets[index]=self.TOMESTONE
                    return t
                return index
            elif self.buckets[index] in [self.TOMESTONE]:
                t=index


            index=self.hash_func(index+1)



    # def find_bucket(self,key:int):
    #     index=self.hash_func(key)
    #     first_tome=-1
    #     while self.buckets[index] is not None:
    #         if self.buckets[index].key==key:
    #             if first_tome !=-1:
    #                 self.buckets[first_tome]=self.buckets[index]
    #                 self.buckets[index]=self.TOMESTONE
    #                 return first_tome
    #             return index
    #         if first_tome==-1 and self.buckets[index] is self.TOMESTONE:
    #             first_tome=index
    #         index=(index+1)%self.capacity
    #     return index if first_tome==-1 else first_tome


    def get(self,key:int):
        index=self.find(key)
        if self.buckets[index] not in [self.TOMESTONE,None]:
            return self.buckets[index].val
    def remove(self,key:int):
        index=self.find(key)
        self.buckets[index]=self.TOMESTONE
        self._size-=1


if __name__ == '__main__':
    hm=HashMapOpenAddressing()
    hm.put(11,'11')
    hm.put(12,'12')
    hm.put(13,'13')
    hm.put(14,'14')
    hm.put(15,'15')
    hm.put(16,'16')
    hm.remove(12)
    hm.put(21,'21')
    hm.remove(21)
    hm.put(31,'31')
    hm.put(31,'32')
    print(hm.get(16))

    hm.extend()
    print(hm.all_set())


def xor_hash(key:str):
    hashh=0
    for i in key:
        #异或运算（XOR）是一种逻辑运算，用于比较两个值的对应位。如果相应位上的两个值相同，则结果为0；如果不同，则结果为1。
        # ord()用于获取字符的 ASCII 码或 Unicode 码值
        #bin()用于将整数转换为二进制字符串
        # hex()将整数转换为十六进制字符串
        hashh^=ord(i)

    return hashh



def hh():
    #hash()->整数和bool的哈希值是其本身
    # 对象的hash值与其内存地址有关
    print(hash(('4')))
    print(0xf)

hh()





