class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.node_height = 1

class AVLTreeStructure:
    def __init__(self):
        self.root_node = None

    def insert_value(self, root, value):
       
        if root is None:
            return TreeNode(value)
        elif value < root.value:
            root.left_child = self.insert_value(root.left_child, value)
        else:
            root.right_child = self.insert_value(root.right_child, value)

        
        root.node_height = 1 + max(self.get_node_height(root.left_child), 
                                   self.get_node_height(root.right_child))

       
        balance = self.check_balance(root)

        
        if balance > 1 and value < root.left_child.value:
            return self.right_rotate(root)

       
        if balance < -1 and value > root.right_child.value:
            return self.left_rotate(root)

        
        if balance > 1 and value > root.left_child.value:
            root.left_child = self.left_rotate(root.left_child)
            return self.right_rotate(root)

        
        if balance < -1 and value < root.right_child.value:
            root.right_child = self.right_rotate(root.right_child)
            return self.left_rotate(root)

        return root

    def delete_value(self, root, value):
        
        if root is None:
            return root

        if value < root.value:
            root.left_child = self.delete_value(root.left_child, value)
        elif value > root.value:
            root.right_child = self.delete_value(root.right_child, value)
        else:
            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                temp = root.left_child
                root = None
                return temp

            temp = self.get_min_node(root.right_child)
            root.value = temp.value
            root.right_child = self.delete_value(root.right_child, temp.value)

        if root is None:
            return root

        
        root.node_height = 1 + max(self.get_node_height(root.left_child), 
                                   self.get_node_height(root.right_child))

        
        balance = self.check_balance(root)

        
        if balance > 1 and self.check_balance(root.left_child) >= 0:
            return self.right_rotate(root)

        
        if balance > 1 and self.check_balance(root.left_child) < 0:
            root.left_child = self.left_rotate(root.left_child)
            return self.right_rotate(root)

        
        if balance < -1 and self.check_balance(root.right_child) <= 0:
            return self.left_rotate(root)

        
        if balance < -1 and self.check_balance(root.right_child) > 0:
            root.right_child = self.right_rotate(root.right_child)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right_child
        T2 = y.left_child

        y.left_child = z
        z.right_child = T2

        z.node_height = 1 + max(self.get_node_height(z.left_child), 
                                self.get_node_height(z.right_child))
        y.node_height = 1 + max(self.get_node_height(y.left_child), 
                                self.get_node_height(y.right_child))

        return y

    def right_rotate(self, z):
        y = z.left_child
        T3 = y.right_child

        y.right_child = z
        z.left_child = T3

        z.node_height = 1 + max(self.get_node_height(z.left_child), 
                                self.get_node_height(z.right_child))
        y.node_height = 1 + max(self.get_node_height(y.left_child), 
                                self.get_node_height(y.right_child))

        return y

    def get_node_height(self, node):
        if not node:
            return 0
        return node.node_height

    def check_balance(self, node):
        if not node:
            return 0
        return self.get_node_height(node.left_child) - self.get_node_height(node.right_child)

    def get_min_node(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current

    def inorder_traversal(self, root):
        elements = []
        if root:
            elements += self.inorder_traversal(root.left_child)
            elements.append(root.value)
            elements += self.inorder_traversal(root.right_child)
        return elements


def avl_tree_program():
    avl_tree = AVLTreeStructure()
    root_node = None

    while True:
        print("\nAVL Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. In-order Traversal")
        print("4. Exit")
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            value = int(input("Enter value to insert: "))
            root_node = avl_tree.insert_value(root_node, value)
            print(f"{value} inserted.")
        elif user_choice == 2:
            value = int(input("Enter value to delete: "))
            root_node = avl_tree.delete_value(root_node, value)
            print(f"{value} deleted.")
        elif user_choice == 3:
            print("In-order Traversal:", avl_tree.inorder_traversal(root_node))
        elif user_choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

avl_tree_program()
