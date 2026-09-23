class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _get_node(self, index: int) -> None | ListNode:
        if index < 0 or index >= self.length:
            return None
        
        mid_index = self.length // 2

        if index <= mid_index:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr
        else:
            reverse_index = (self.length - 1) - index
            curr = self.tail
            for _ in range(reverse_index):
                curr = curr.prev
            return curr

    def get(self, index: int) -> int:
        node = self._get_node(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        if self.length == 0:
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.tail
        if self.length == 0:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        
        curr = self._get_node(index)
        newNode = ListNode(val)
        newNode.prev = curr.prev
        newNode.next = curr
        curr.prev.next = newNode
        curr.prev = newNode
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        if index == 0:
            if self.length > 1:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node = self._get_node(index)
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)