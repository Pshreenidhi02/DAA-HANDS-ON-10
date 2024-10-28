class RBTNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent_node = None
        self.color_flag = 'RED'

class RBTree:
    def __init__(self):
        self.leaf = RBTNode(0)
        self.leaf.color_flag = 'BLACK'
        self.main_root = self.leaf

    def add(self, value):
        new_entry = RBTNode(value)
        new_entry.left_child = self.leaf
        new_entry.right_child = self.leaf
        self._insert_node_bst(new_entry)
        self._repair_insert(new_entry)

    def _insert_node_bst(self, node):
        parent_ref = None
        current_ref = self.main_root

        while current_ref != self.leaf:
            parent_ref = current_ref
            if node.value < current_ref.value:
                current_ref = current_ref.left_child
            else:
                current_ref = current_ref.right_child

        node.parent_node = parent_ref
        if parent_ref is None:
            self.main_root = node
        elif node.value < parent_ref.value:
            parent_ref.left_child = node
        else:
            parent_ref.right_child = node

    def _repair_insert(self, node):
        while node != self.main_root and node.parent_node.color_flag == 'RED':
            if node.parent_node == node.parent_node.parent_node.left_child:
                sibling_node = node.parent_node.parent_node.right_child
                if sibling_node.color_flag == 'RED':
                    node.parent_node.color_flag = 'BLACK'
                    sibling_node.color_flag = 'BLACK'
                    node.parent_node.parent_node.color_flag = 'RED'
                    node = node.parent_node.parent_node
                else:
                    if node == node.parent_node.right_child:
                        node = node.parent_node
                        self._left_rotate(node)
                    node.parent_node.color_flag = 'BLACK'
                    node.parent_node.parent_node.color_flag = 'RED'
                    self._right_rotate(node.parent_node.parent_node)
            else:
                sibling_node = node.parent_node.parent_node.left_child
                if sibling_node.color_flag == 'RED':
                    node.parent_node.color_flag = 'BLACK'
                    sibling_node.color_flag = 'BLACK'
                    node.parent_node.parent_node.color_flag = 'RED'
                    node = node.parent_node.parent_node
                else:
                    if node == node.parent_node.left_child:
                        node = node.parent_node
                        self._right_rotate(node)
                    node.parent_node.color_flag = 'BLACK'
                    node.parent_node.parent_node.color_flag = 'RED'
                    self._left_rotate(node.parent_node.parent_node)
        self.main_root.color_flag = 'BLACK'

    def remove(self, value):
        node_to_delete = self.locate(self.main_root, value)
        if node_to_delete == self.leaf:
            print(f"{value} not found in the Red-Black Tree. No deletion performed.")
            return
        self._delete_entry(node_to_delete)

    def _delete_entry(self, node):
        initial_color = node.color_flag
        if node.left_child == self.leaf:
            substitute = node.right_child
            self._shift_parent(node, node.right_child)
        elif node.right_child == self.leaf:
            substitute = node.left_child
            self._shift_parent(node, node.left_child)
        else:
            successor = self.find_min(node.right_child)
            initial_color = successor.color_flag
            substitute = successor.right_child
            if successor.parent_node == node:
                substitute.parent_node = successor
            else:
                self._shift_parent(successor, successor.right_child)
                successor.right_child = node.right_child
                successor.right_child.parent_node = successor
            self._shift_parent(node, successor)
            successor.left_child = node.left_child
            successor.left_child.parent_node = successor
            successor.color_flag = node.color_flag

        if initial_color == 'BLACK':
            self._repair_delete(substitute)

    def _shift_parent(self, u, v):
        if u.parent_node is None:
            self.main_root = v
        elif u == u.parent_node.left_child:
            u.parent_node.left_child = v
        else:
            u.parent_node.right_child = v
        v.parent_node = u.parent_node

    def _repair_delete(self, node):
        while node != self.main_root and node.color_flag == 'BLACK':
            if node == node.parent_node.left_child:
                sibling = node.parent_node.right_child
                if sibling.color_flag == 'RED':
                    sibling.color_flag = 'BLACK'
                    node.parent_node.color_flag = 'RED'
                    self._left_rotate(node.parent_node)
                    sibling = node.parent_node.right_child
                if sibling.left_child.color_flag == 'BLACK' and sibling.right_child.color_flag == 'BLACK':
                    sibling.color_flag = 'RED'
                    node = node.parent_node
                else:
                    if sibling.right_child.color_flag == 'BLACK':
                        sibling.left_child.color_flag = 'BLACK'
                        sibling.color_flag = 'RED'
                        self._right_rotate(sibling)
                        sibling = node.parent_node.right_child
                    sibling.color_flag = node.parent_node.color_flag
                    node.parent_node.color_flag = 'BLACK'
                    sibling.right_child.color_flag = 'BLACK'
                    self._left_rotate(node.parent_node)
                    node = self.main_root
            else:
                sibling = node.parent_node.left_child
                if sibling.color_flag == 'RED':
                    sibling.color_flag = 'BLACK'
                    node.parent_node.color_flag = 'RED'
                    self._right_rotate(node.parent_node)
                    sibling = node.parent_node.left_child
                if sibling.right_child.color_flag == 'BLACK' and sibling.left_child.color_flag == 'BLACK':
                    sibling.color_flag = 'RED'
                    node = node.parent_node
                else:
                    if sibling.left_child.color_flag == 'BLACK':
                        sibling.right_child.color_flag = 'BLACK'
                        sibling.color_flag = 'RED'
                        self._left_rotate(sibling)
                        sibling = node.parent_node.left_child
                    sibling.color_flag = node.parent_node.color_flag
                    node.parent_node.color_flag = 'BLACK'
                    sibling.left_child.color_flag = 'BLACK'
                    self._right_rotate(node.parent_node)
                    node = self.main_root
        node.color_flag = 'BLACK'

    def locate(self, node, value):
        if node == self.leaf or node.value == value:
            return node
        if value < node.value:
            return self.locate(node.left_child, value)
        return self.locate(node.right_child, value)

    def find_min(self, node):
        while node.left_child != self.leaf:
            node = node.left_child
        return node

    def inorder_display(self, node, result):
        if node != self.leaf:
            self.inorder_display(node.left_child, result)
            result.append(node.value)
            self.inorder_display(node.right_child, result)
        return result

    def _left_rotate(self, node):
        temp = node.right_child
        node.right_child = temp.left_child
        if temp.left_child != self.leaf:
            temp.left_child.parent_node = node
        temp.parent_node = node.parent_node
        if node.parent_node is None:
            self.main_root = temp
        elif node == node.parent_node.left_child:
            node.parent_node.left_child = temp
        else:
            node.parent_node.right_child = temp
        temp.left_child = node
        node.parent_node = temp

    def _right_rotate(self, node):
        temp = node.left_child
        node.left_child = temp.right_child
        if temp.right_child != self.leaf:
            temp.right_child.parent_node = node
        temp.parent_node = node.parent_node
        if node.parent_node is None:
            self.main_root = temp
        elif node == node.parent_node.right_child:
            node.parent_node.right_child = temp
        else:
            node.parent_node.left_child = temp
        temp.right_child = node
        node.parent_node = temp


def rbt_demo():
    rbt = RBTree()
    while True:
        print("\nRed-Black Tree Operations:")
        print("1. Add")
        print("2. Remove")
        print("3. Locate")
        print("4. Display In-order")
        print("5. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            value = int(input("Enter value to add: "))
            rbt.add(value)
            print(f"{value} added.")
        elif choice == 2:
            value = int(input("Enter value to remove: "))
            rbt.remove(value)
        elif choice == 3:
            value = int(input("Enter value to locate: "))
            found_node = rbt.locate(rbt.main_root, value)
            print(f"{value} found." if found_node != rbt.leaf else f"{value} not found.")
        elif choice == 4:
            print("In-order Display:", rbt.inorder_display(rbt.main_root, []))
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

rbt_demo()
