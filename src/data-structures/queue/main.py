from typing import Any

class Queue:
    def __init__(self):
        self.queue = []
    
    def append(self, data: Any) -> None:
        self.queue.append(data)
    
    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)
    
    def __str__(self) -> str:
        return self.queue.__str__()

if __name__ == '__main__':
    q = Queue()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())