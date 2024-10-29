class RBTNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent_node = None
        self.node_color = 'RED'

class RedBlackTree:
    def __init__(self):
        self.nil_leaf = RBTNode(0)
        self.nil_leaf.node_color = 'BLACK'
        self.root_node = self.nil_leaf

    def insert(self, value):
        new_node = RBTNode(value)
        new_node.left_child = self.nil_leaf
        new_node.right_child = self.nil_leaf
        self._insert_bst(new_node)
        self._fix_insert(new_node)

    def _insert_bst(self, node):
        parent_node = None
        current_node = self.root_node

        while current_node != self.nil_leaf:
            parent_node = current_node
            if node.value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        node.parent_node = parent_node
        if parent_node is None:
            self.root_node = node
        elif node.value < parent_node.value:
            parent_node.left_child = node
        else:
            parent_node.right_child = node

    def _fix_insert(self, node):
        while node != self.root_node and node.parent_node.node_color == 'RED':
            if node.parent_node == node.parent_node.parent_node.left_child:
                uncle = node.parent_node.parent_node.right_child
                if uncle.node_color == 'RED':
                    node.parent_node.node_color = 'BLACK'
                    uncle.node_color = 'BLACK'
                    node.parent_node.parent_node.node_color = 'RED'
                    node = node.parent_node.parent_node
                else:
                    if node == node.parent_node.right_child:
                        node = node.parent_node
                        self._rotate_left(node)
                    node.parent_node.node_color = 'BLACK'
                    node.parent_node.parent_node.node_color = 'RED'
                    self._rotate_right(node.parent_node.parent_node)
            else:
                uncle = node.parent_node.parent_node.left_child
                if uncle.node_color == 'RED':
                    node.parent_node.node_color = 'BLACK'
                    uncle.node_color = 'BLACK'
                    node.parent_node.parent_node.node_color = 'RED'
                    node = node.parent_node.parent_node
                else:
                    if node == node.parent_node.left_child:
                        node = node.parent_node
                        self._rotate_right(node)
                    node.parent_node.node_color = 'BLACK'
                    node.parent_node.parent_node.node_color = 'RED'
                    self._rotate_left(node.parent_node.parent_node)
        self.root_node.node_color = 'BLACK'

    def delete(self, value):
        node = self.search(self.root_node, value)
        if node == self.nil_leaf:
            print(f"{value} not found in the Red-Black Tree. Deletion not performed.")
            return
        self._delete_node(node)

    def _delete_node(self, node):
        original_color = node.node_color
        if node.left_child == self.nil_leaf:
            temp_node = node.right_child
            self._transplant(node, node.right_child)
        elif node.right_child == self.nil_leaf:
            temp_node = node.left_child
            self._transplant(node, node.left_child)
        else:
            successor = self.min_value_node(node.right_child)
            original_color = successor.node_color
            temp_node = successor.right_child
            if successor.parent_node == node:
                temp_node.parent_node = successor
            else:
                self._transplant(successor, successor.right_child)
                successor.right_child = node.right_child
                successor.right_child.parent_node = successor
            self._transplant(node, successor)
            successor.left_child = node.left_child
            successor.left_child.parent_node = successor
            successor.node_color = node.node_color

        if original_color == 'BLACK':
            self._fix_delete(temp_node)

    def _transplant(self, u, v):
        if u.parent_node is None:
            self.root_node = v
        elif u == u.parent_node.left_child:
            u.parent_node.left_child = v
        else:
            u.parent_node.right_child = v
        v.parent_node = u.parent_node

    def _fix_delete(self, node):
        while node != self.root_node and node.node_color == 'BLACK':
            if node == node.parent_node.left_child:
                sibling = node.parent_node.right_child
                if sibling.node_color == 'RED':
                    sibling.node_color = 'BLACK'
                    node.parent_node.node_color = 'RED'
                    self._rotate_left(node.parent_node)
                    sibling = node.parent_node.right_child
                if sibling.left_child.node_color == 'BLACK' and sibling.right_child.node_color == 'BLACK':
                    sibling.node_color = 'RED'
                    node = node.parent_node
                else:
                    if sibling.right_child.node_color == 'BLACK':
                        sibling.left_child.node_color = 'BLACK'
                        sibling.node_color = 'RED'
                        self._rotate_right(sibling)
                        sibling = node.parent_node.right_child
                    sibling.node_color = node.parent_node.node_color
                    node.parent_node.node_color = 'BLACK'
                    sibling.right_child.node_color = 'BLACK'
                    self._rotate_left(node.parent_node)
                    node = self.root_node
            else:
                sibling = node.parent_node.left_child
                if sibling.node_color == 'RED':
                    sibling.node_color = 'BLACK'
                    node.parent_node.node_color = 'RED'
                    self._rotate_right(node.parent_node)
                    sibling = node.parent_node.left_child
                if sibling.right_child.node_color == 'BLACK' and sibling.left_child.node_color == 'BLACK':
                    sibling.node_color = 'RED'
                    node = node.parent_node
                else:
                    if sibling.left_child.node_color == 'BLACK':
                        sibling.right_child.node_color = 'BLACK'
                        sibling.node_color = 'RED'
                        self._rotate_left(sibling)
                        sibling = node.parent_node.left_child
                    sibling.node_color = node.parent_node.node_color
                    node.parent_node.node_color = 'BLACK'
                    sibling.left_child.node_color = 'BLACK'
                    self._rotate_right(node.parent_node)
                    node = self.root_node
        node.node_color = 'BLACK'

    def search(self, node, value):
        if node == self.nil_leaf or node.value == value:
            return node
        if value < node.value:
            return self.search(node.left_child, value)
        return self.search(node.right_child, value)

    def min_value_node(self, node):
        while node.left_child != self.nil_leaf:
            node = node.left_child
        return node

    def inorder_traversal(self, node, result):
        if node != self.nil_leaf:
            self.inorder_traversal(node.left_child, result)
            result.append(node.value)
            self.inorder_traversal(node.right_child, result)
        return result

    def _rotate_left(self, node):
        y = node.right_child
        node.right_child = y.left_child
        if y.left_child != self.nil_leaf:
            y.left_child.parent_node = node
        y.parent_node = node.parent_node
        if node.parent_node is None:
            self.root_node = y
        elif node == node.parent_node.left_child:
            node.parent_node.left_child = y
        else:
            node.parent_node.right_child = y
        y.left_child = node
        node.parent_node = y

    def _rotate_right(self, node):
        y = node.left_child
        node.left_child = y.right_child
        if y.right_child != self.nil_leaf:
            y.right_child.parent_node = node
        y.parent_node = node.parent_node
        if node.parent_node is None:
            self.root_node = y
        elif node == node.parent_node.right_child:
            node.parent_node.right_child = y
        else:
            node.parent_node.left_child = y
        y.right_child = node
        node.parent_node = y

def rbt_program():
    rbt = RedBlackTree()
    while True:
        print("\nRed-Black Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. In-order Traversal")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to insert: "))
            rbt.insert(value)
            print(f"{value} inserted.")
        elif choice == 2:
            value = int(input("Enter value to delete: "))
            rbt.delete(value)
        elif choice == 3:
            value = int(input("Enter value to search: "))
            found_node = rbt.search(rbt.root_node, value)
            if found_node != rbt.nil_leaf:
                print(f"{value} found in Red-Black Tree.")
            else:
                print(f"{value} not found in Red-Black Tree.")
        elif choice == 4:
            print("In-order Traversal:", rbt.inorder_traversal(rbt.root_node, []))
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

rbt_program()
