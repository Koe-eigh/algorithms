from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, data: Any, next_node: Node=None) -> None:
        self.data = data
        self.next = next_node
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head: Node=None) -> None:
        self.head = head
    
    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def insert(self, data: Any, index: int=0) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        pointer: Node = self.head
        for _ in range(index-1):
            pointer = pointer.next
        new_node.next = pointer.next
        pointer.next = new_node
    
    def remove(self, data: Any) -> None:
        pointer: Node = self.head
        prev_node: Node = self.head
        while pointer.data != data:
            prev_node = pointer
            pointer = pointer.next
        prev_node.next = pointer.next
    
    def get(self, index: int) -> Any:
        pointer: Node = self.head
        for _ in range(index):
            pointer = pointer.next
        return pointer
    
    def length(self) -> int:
        counter: int = 0
        pointer: Node = self.head
        while pointer is not None:
            counter += 1
            pointer = pointer.next
        return counter
    
    def print(self) -> None:
        pointer: Node = self.head
        while pointer is not None:
            print(pointer.data, end=', ')
            pointer = pointer.next
        print()

    def reverse(self) -> None:
        if self.length() == 0 or self.length() == 1:
            return
        prev: Node = None
        current: Node = self.head
        while current:
            next = current.next
            current.next = prev

            prev = current
            current = next
        self.head = prev

    def reverse_even(self) -> None:
        def _reverse(begin: Node, end: Node):
            prev: Node = None
            current: Node = begin
            while current != end:
                next: Node = current.next
                current.next = prev
                prev = current
                current = next
            return prev

        prev: Node = None
        current: Node = self.head
        while current:
            if current.data % 2 == 0:
                even_start = current
                while current and current.data % 2 == 0:
                    current = current.next
                even_end = current

                reversed_head = _reverse(even_start, even_end)

                if prev is not None:
                    prev.next = reversed_head
                else:
                    self.head = reversed_head
                even_start.next = even_end

                prev = even_start
            else:
                prev = current
                current = current.next

if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.print()
    l.append(5)
    l.print()
    l.append(7)
    l.print()
    l.append(14)
    l.print()
    l.append(12)
    l.print()
    l.append(10)
    l.print()
    l.append(2)
    l.print()
    l.insert(8, index=1)
    l.print()
    l.remove(5)
    l.print()
    l.reverse()
    l.print()
    l.reverse_even()
    l.print()
    print(f"index=1 --> {l.get(1)}")