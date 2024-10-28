class BinarySearchTree:
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, current_node, value):
        if not current_node:
            return self.TreeNode(value)
        if value < current_node.value:
            current_node.left = self._insert(current_node.left, value)
        else:
            current_node.right = self._insert(current_node.right, value)
        return current_node

    def search(self, key):
        return self._search(self.root, key) is not None

    def _search(self, current_node, key):
        if not current_node or current_node.value == key:
            return current_node
        if key < current_node.value:
            return self._search(current_node.left, key)
        return self._search(current_node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, current_node, key):
        if not current_node:
            return current_node
        if key < current_node.value:
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node.value:
            current_node.right = self._delete(current_node.right, key)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            temp = self._min_value_node(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete(current_node.right, temp.value)
        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, current_node):
        if current_node:
            self._inorder_traversal(current_node.left)
            print(current_node.value, end=' ')
            self._inorder_traversal(current_node.right)


# Testing the Binary Search Tree with different values
def test_bst():
    print("Binary Search Tree Testing")
    bst = BinarySearchTree()
    
    # Insert values
    bst.insert(45)
    bst.insert(32)
    bst.insert(18)
    bst.insert(39)
    bst.insert(60)
    bst.insert(55)
    bst.insert(72)
    
    print("Inorder traversal after insertions:")
    bst.inorder_traversal()
    
    # Delete specific values
    bst.delete(18)
    print("Inorder traversal after deleting 18:")
    bst.inorder_traversal()
    
    bst.delete(32)
    print("Inorder traversal after deleting 32:")
    bst.inorder_traversal()
    
    bst.delete(45)
    print("Inorder traversal after deleting 45:")
    bst.inorder_traversal()
    
    # Search for values
    print("Search for 60:", "Found" if bst.search(60) else "Not Found")
    print("Search for 100:", "Found" if bst.search(100) else "Not Found")


# Run the test
test_bst()
