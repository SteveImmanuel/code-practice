# https://leetcode.com/problems/design-circular-queue/

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.current_capacity = 0
        self.f_ptr = None
        self.r_ptr = None        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = Node(value)
        if not self.isEmpty():
            new_node.next = self.r_ptr.next
            self.r_ptr.next = new_node
            self.r_ptr = self.r_ptr.next
        else:
            self.f_ptr = new_node
            self.r_ptr = new_node
            self.f_ptr.next = new_node
            self.r_ptr.next = new_node

        self.current_capacity += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.current_capacity == 1:
            self.f_ptr = None
            self.r_ptr = None
        else:
            self.r_ptr.next = self.f_ptr.next
            self.f_ptr = self.f_ptr.next
            
        self.current_capacity -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.f_ptr.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.r_ptr.val

    def isEmpty(self) -> bool:
        return self.current_capacity == 0

    def isFull(self) -> bool:
        return self.capacity == self.current_capacity
        


myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))
print(myCircularQueue.enQueue(2))
print(myCircularQueue.enQueue(3))
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear()    )
print(myCircularQueue.isFull()  )
print(myCircularQueue.deQueue() )
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear()    )