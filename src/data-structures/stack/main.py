from typing import Any

class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def append(self, data: Any) -> None:
        self.stack.append(data)
    
    def pop(self) -> Any:
        if self.stack != []:
            return self.stack.pop()
    
    def __str__(self) -> str:
        return self.stack.__str__()

if __name__ == '__main__':
    s = Stack()
    print(s)
    s.append(1)
    print(s)
    s.append(2)
    print(s)
    print(s.pop())
    print(s)
