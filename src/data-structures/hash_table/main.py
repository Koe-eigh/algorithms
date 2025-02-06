from __future__ import annotations
import hashlib

class HashTable[K, V]:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.tables = [[] for _ in range(size)]
    
    def set(self, key: K, value: V) -> None:
        hash = int(hashlib.sha256(key.encode()).hexdigest(), 16) % self.size
        for table in self.tables:
            if table == []: continue
            for pair in table:
                if pair[0] == key:
                    pair[1] = value
                    return
        self.tables[hash].append([key, value])
    
    def get(self, key: K) -> V:
        hash = int(hashlib.sha256(key.encode()).hexdigest(), 16) % self.size
        table = self.tables[hash]
        if table != []:
            for pair in table:
                if pair[0] == key:
                    return pair[1]
        raise KeyError(f"The given key '{key}' does not exit in the table.")
    
    def print(self) -> None:
        for i in range(self.size):
            print(f"{i} -->", end=' ')
            print(self.tables[i])


if __name__ == '__main__':
    ht = HashTable[str, str]()
    ht.set('hoge', 'moge')
    ht.set('hoge', 'fuga')
    ht.set('boo', 'foo')
    print(ht.get('moge'))