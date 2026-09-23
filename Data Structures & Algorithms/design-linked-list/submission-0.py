class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    #O(n) where n is the length of the list
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        elif index == self.length - 1:
            return self.tail.val
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.val
        
    # O(1)
    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        if not self.tail:
            self.tail = newNode
        
    # O(1)
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.length += 1
        if not self.tail:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    # O(n) where n is the length of the list
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            newNode = ListNode(val)
            newNode.next = prev.next
            prev.next = newNode
            self.length += 1

    # O(n) where n is the length of the list
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        if index == 0 and self.length > 1:
            self.head = self.head.next
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
            if index == self.length - 1:
                self.tail = prev
        
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)