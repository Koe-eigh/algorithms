class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node = None
        self.right: Node = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return
        
        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value)
            
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            
            return node
        
        _insert(self.root, value)
    
    def remove(self, value: int) -> None:
        def _min_value(node: Node) -> Node:
            current = node
            while current.left:
                current = current.left
            return current

        def _remove(node: Node, value: int) -> Node:
            if node is None:
                return node
            
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                tmp = _min_value(node.right)
                node.value = tmp.value
                node.right = _remove(node.right, tmp.value)
            return node
        _remove(self.root, value)

    
    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False
            
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            elif value > node.value:
                return _search(node.right, value)
        
        return _search(self.root, value)
    
    def inorder(self) -> None:
        def _inorder(node: Node) -> Node:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)

        _inorder(self.root)

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(1)
    tree.insert(6)
    tree.insert(9)
    tree.insert(4)
    tree.insert(2)
    tree.inorder()
    print(tree.search(6))
    print('######## Remove')
    tree.remove(6)
    tree.inorder()
    print(tree.search(6))