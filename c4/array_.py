import random


arr:list[int]=[0]*5
arr2:list[int]=[1,2,3,4,5]

# get an random element
def random_access(nums:list[int])->int:
    random_index=random.randint(0,len(nums)-1)
    random_num=nums[random_index]
    return random_num

# insert an element,but will lose the last element
def insert(nums:list[int],num:int,index:int):
    for i in range(len(nums)-1,index,-1):
        print(i)
        nums[i]=nums[i-1]
    nums[index]=num
    return nums

# delete an element
def delete(nums:list[int],index):
    for i in range(index,len(nums)-1):
        nums[i]=nums[i+1]
    nums[len(nums)-1]=0
    return nums

# traverse all elements
def traverse(nums:list[int]):
    for i in range(0,len(nums)):
        print(nums[i])

def find(nums:list[int],num:int)->int:
    count=0
    for i in nums:
        if i ==num:
            return count
        count+=1
    return None


def extend(nums:list[int],num:int)->list[int]:
    new_nums:list[int]=[0]*(len(nums)+num)
    for i in range(len(nums)):
        new_nums[i]=nums[i]
    return new_nums


if __name__ == '__main__':
    print(extend(arr2,10))