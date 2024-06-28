import random
#蒙特卡洛算法？
sorce_list=[]

def lab():
    li:list[int]=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    sorce:int=0
    for i in range(1,11):
        answer=random.sample(li,1)[0]
        li.remove(answer)
        if i==answer:
            sorce+=1
    return sorce



if __name__ == '__main__':
    for i in range(1000000):
        sorce_list.append(lab())
    print(sorce_list)
    print(sum(sorce_list)/len(sorce_list))
    print(10 in sorce_list)