class MyCircularQueue:

    def __init__(self, k: int):
        self.que, self.count , self.front, self.rear = [0] * k, 0, 0, 0
    def enQueue(self, value: int) -> bool:
        if self.count == len(self.que):
            return False
        ind = self.rear % len(self.que)
        self.count += 1
        self.que[ind] = value
        self.rear += 1
        return True
    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.count -=  1
        self.front += 1
        return True
    def Front(self) -> int:
        if self.count == 0:
            return -1
        ind = self.front % len(self.que)
        return self.que[ind]
    def Rear(self) -> int:
        if self.count == 0:
            return -1
        ind = self.rear % len(self.que) - 1
        return self.que[ind]
    def isEmpty(self) -> bool:
        return self.count == 0
    def isFull(self) -> bool:
        return self.count == len(self.que)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()