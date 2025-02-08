from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self, head: Node = None):
        self.head = head
    
    def append(self, data: Any) -> None:
        """
        最後尾にdataを挿入します
        """
        new_node = Node(data)
        if self.length() == 0:
            self.head = new_node
            return
        pointer: Node = self.head
        for _ in range(self.length() - 1):
            pointer = pointer.next
        pointer.next = new_node
        new_node.prev = pointer
    
    def get(self, index: int) -> Any:
        """
        指定したindeのdataを取得します。
        """
        if index >= self.length(): raise IndexError(f"Index out of bounds. the argument must be less than {self.length() - 1}")
        pointer: Node = self.head
        for _ in range(index):
            pointer = pointer.next
        return pointer.data
    
    def insert(self, data: Any, index: int = 0) -> None:
        """
        指定したindexにdataを挿入します。
        """
        if index > self.length(): raise IndexError(f"Index out of bounds. the argument must be less than {self.length() - 1}")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head.next.prev = new_node
            self.head = new_node
            return
        
        if index == self.length():
            self.append(data)
            return

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.prev.next = new_node
        new_node.prev = current_node.prev
        new_node.next = current_node
    
    def sort(self) -> None:
        if self.length == 0 or self.length == 1:
            return
        

    def length(self) -> int:
        """
        listの大きさを返します。
        """
        count = 0
        pointer: Node = self.head
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count
    
    def print(self) -> None:
        pointer: Node = self.head
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next

if __name__ == '__main__':
    l = DoublyLinkedList()
    l.append(1)
    l.append(4)
    l.append(3)
    l.insert(7, 3)
    l.print()
