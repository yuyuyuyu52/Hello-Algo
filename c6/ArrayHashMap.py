# 思考，哈希表是用于高效的元素查询，输入一个键从而获取一个值，例如输入学号获取姓名
# 如果让我自己实现该功能，我会
class MyHashMap:
    def __init__(self):
        self.id_list=[]
        self.name_list=[]

    def push(self,key:int,value:str):
        self.id_list.append(key)
        self.name_list.append(value)

    #此处查找value的复杂程度为O(n),故我自己能实现哈希表，但是效率不及哈希表，哈希表的查找复杂度是O(1)
    def get(self,key:int):
        count=0
        for i in self.id_list:
            if i==key:
                return self.name_list[count]
            count+=1
        return

class Pair:
    def __init__(self,key:int,val:str):
        self.key:int=key
        self.val:str=val
class HashMap:
    def __init__(self,capacity:int):
        self.buckets:list[Pair|None]=[None]*capacity
        self._size:int=0

    def hash_func(self, key:int):
        return (key%len(self.buckets))


    def put(self,key:int,val:str):
        pair=Pair(key,val)
        self.buckets[self.hash_func(key)]=pair


    def get(self,key:int):
        pair=self.buckets[self.hash_func(key)]
        if pair is None:
            return
        return pair.val


    def remove(self,key:int):
        self.buckets[self.hash_func(key)]=None


    def all_set(self):
        arr=[]
        for i in self.buckets:
            if not i is None:
                t=(i.key,i.val)
                arr.append(t)
        return arr

    def key_set(self):
        arr=[]
        for i in self.buckets:
            if not i is None:
                arr.append(i.key)
        return arr

    def val_set(self):
        arr=[]
        for i in self.buckets:
            if not i is None:
                arr.append(i.val)
        return arr











if __name__ == '__main__':
    hm=HashMap(100)
    hm.put(3081377916,'will')
    hm.put(3081377934,'jeo')
    hm.remove(3081377916)
    print(hm.all_set())
    print(hm.get(3081377916))
    print(hm.buckets)
