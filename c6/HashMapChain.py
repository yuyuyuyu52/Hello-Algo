from ArrayHashMap import Pair

class HashMapChain:
    def __init__(self):
        # 在Python中，使用乘法操作符 * 来创建一个包含多个子列表的列表时，可能会导致意外行为，因为它复制的是相同的子列表的引用，
        # 而不是创建独立的子列表。这意味着修改一个子列表会影响到所有的引用该子列表的地方。
        # 所以对于可变对象，推荐使用列表推导式来确保每个元素都是独立的对象
        # 包括列表、字典、集合、自定义类的实例、以及其他可变对象
        self._size:int=0
        self.capacity:int=3
        self.load_thres:float=2/3
        self.extend_ratio:int=2
        self.buckets:list[list[Pair]]=[[] for i in range(self.capacity)]


    def extend(self):
        self.capacity=self.capacity*self.extend_ratio
        new_buckets:list[list[Pair]]=[[] for i in range(self.capacity)]
        for key,val in self.all_set():
            pair = Pair(key, val)
            new_buckets[self.hash_func(key)].append(pair)
        self.buckets=new_buckets




    def hash_func(self,key:int):
        return key%self.capacity

    def put(self,key:int,val:str):
        if self._size/self.capacity>=self.load_thres:
            self.extend()
        pair=Pair(key,val)
        self.buckets[self.hash_func(key)].append(pair)
        self._size+=1

    def get(self,key:int):
        for i in self.buckets[self.hash_func(key)]:
            if i.key==key:
                return i.val
        return 'No this student'

    def all_set(self):
        arr=[]
        for i in self.buckets:
            if not len(i) ==0:
                for _ in i:
                    arr.append((_.key,_.val))
        return arr


if __name__ == '__main__':
    hm=HashMapChain()
    hm.put(200,'200')
    hm.put(100,'100')
    hm.put(101,'101')
    print(hm.buckets)
    print(hm.all_set())

