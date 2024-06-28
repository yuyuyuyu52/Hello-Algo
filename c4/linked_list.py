# `num: int` 和 `num` 之间有以下不同：
#
# 1. **`num: int` (类型提示):**
#    - **目的:** 提供关于变量预期类型的信息。对于文档编写、代码可读性非常有用，并且可以被静态类型检查器（例如 `mypy`）用于在代码运行之前捕获类型错误。
#    - **实际作用:** 帮助开发人员理解代码的预期使用方式，并在开发过程中避免类型错误。静态类型检查工具可以利用这些类型提示来检查代码的正确性。
#
# 2. **`num` (普通变量声明):**
#    - **目的:** 只是声明一个变量，没有任何类型信息。
#    - **实际作用:** 只是在代码中创建了一个变量，类型信息只能通过运行时确定，可能导致在开发过程中出现类型错误而不易发现。


# `self.next: ListNode | None = None` 这行代码使用了类型提示和默认值，具体作用如下：
#
# 1. **`self.next: ListNode | None`:**
#    - **目的:** 指定 `self.next` 属性的预期类型。类型提示 `ListNode | None` 表示 `self.next` 可以是一个 `ListNode` 实例或者 `None`。
#    - **实际作用:** 提高代码可读性，帮助开发者和静态类型检查工具理解 `self.next` 的预期类型，避免类型错误。
#
# 2. **`= None`:**
#    - **目的:** 为 `self.next` 属性设置默认值 `None`。
#    - **实际作用:** 在实例化 `ListNode` 对象时，如果没有显式设置 `self.next`，它将默认被初始化为 `None`。
#
# 综合起来，这行代码的完整作用是：
# - 在 `ListNode` 类的 `__init__` 方法中，初始化 `self.next` 属性，并明确表示它的类型可以是 `ListNode` 或者 `None`，且默认值为 `None`。

class ListNode:
    def __init__(self,num:int):
        self.num:int =num
        self.next:ListNode |None=None

n0=ListNode(0)
n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)

n0.next=n1
n1.next=n2
n2.next=n3
n3.next=n4

def insert(listnode1:ListNode,num:int):
    P=ListNode(num)
    P.next=listnode1.next
    listnode1.next=P

def delete(listnode:ListNode):
    if not listnode.next:
        return
    listnode.next=listnode.next.next

def access(head:ListNode,index:int)->ListNode|None:
    target=head
    for i in range(index):
        if not target:
            return
        target=target.next
    return target


def find(head:ListNode,num):
    count=0
    while head:
        if head.num==num:
            return count
        count+=1
        head=head.next
    return


# 如果直接写print(1)那么在别的程序中导入ListNode类时，会多输出1
# 如果把print(1)放入main block中则不会
if __name__ == '__main__':
    print(find(n0,5))

