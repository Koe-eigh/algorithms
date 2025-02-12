import sys
from typing import Optional

class MiniHeap:
    def __init__(self) -> None:
        self.heap = [-sys.maxsize]
        self.size = 0
    
    def parent_index(self, index: int) -> int:
        return index // 2
    
    def left_child_index(self, index: int) -> int:
        return index * 2
    
    def right_child_index(self, index: int) -> int:
        return (index * 2) + 1
    
    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def smaller_child_index(self, index: int) -> int:
        if self.right_child_index(index) > self.size:
            return self.left_child_index(index)
        else:
            if self.right_child_index(index) < self.left_child_index(index):
                return self.right_child_index(index)
            else:
                return self.left_child_index(index)
    
    def heapify_down(self, index: int) -> None:
        while self.left_child_index(index) <= self.size:
            smaller_child_index = self.smaller_child_index(index)
            if self.heap[smaller_child_index] < self.heap[index]:
                self.swap(index, smaller_child_index)
            index = smaller_child_index
    
    def push(self, value: int) -> None:
        self.heap.append(value)
        self.size += 1
        self.heapify_up(self.size)
    
    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return
        
        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root
        
        self.heap[1] = data
        self.size -= 1
        self.heapify_down(1)
        
        return root
        


    def __str__(self) -> str:
        return str([self.heap[i] for i in range(1, self.size+1)])

if __name__ == '__main__':
    heap = MiniHeap()
    heap.push(7)
    heap.push(1)
    heap.push(9)
    heap.push(6)
    heap.push(2)
    heap.push(3)
    heap.push(4)
    print(heap)
    print(heap.pop())
    print(heap)