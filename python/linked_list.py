class Node:

    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

        
    def get(self, index: int) -> int:
        if not self.head or self.size < index:
            return -1
        next = self.head
        i = 0
        while next:
            i += 1
            if i == index:
                return next.next.val
            next = next.next
        return -1


    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.head = node
        
        next = self.head
        while next:
            if not next.next:
                next.next = node
                break
            next = next.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        next = self.head
        node = Node(val)
        while next:
            i += 1
            if i == index:
                node.next = next.next
                next.next = node
                break
            next = next.next
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if self.size >= index:
            i = 0
            next = self.head
            while next:
                i += 1
                if i == index:
                    next.next = next.next.next
                    self.size -=1
                    break
                next = next.next
