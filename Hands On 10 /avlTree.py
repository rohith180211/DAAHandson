class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.node_height = 1

class AVLTree:
    def insert(self, root, value):
        if not root:
            return AVLNode(value)
        elif value < root.value:
            root.left_child = self.insert(root.left_child, value)
        else:
            root.right_child = self.insert(root.right_child, value)

        root.node_height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))
        balance_factor = self.get_balance(root)

        if balance_factor > 1 and value < root.left_child.value:
            return self.rotate_right(root)

        if balance_factor < -1 and value > root.right_child.value:
            return self.rotate_left(root)

        if balance_factor > 1 and value > root.left_child.value:
            root.left_child = self.rotate_left(root.left_child)
            return self.rotate_right(root)

        if balance_factor < -1 and value < root.right_child.value:
            root.right_child = self.rotate_right(root.right_child)
            return self.rotate_left(root)

        return root

    def delete(self, root, value):
        if not root:
            print(f"{value} not found in AVL Tree.")
            return root

        if value < root.value:
            root.left_child = self.delete(root.left_child, value)
        elif value > root.value:
            root.right_child = self.delete(root.right_child, value)
        else:
            if not root.left_child:
                return root.right_child
            elif not root.right_child:
                return root.left_child

            temp = self.find_min_node(root.right_child)
            root.value = temp.value
            root.right_child = self.delete(root.right_child, temp.value)

        if not root:
            return root

        root.node_height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))
        balance_factor = self.get_balance(root)

        if balance_factor > 1 and self.get_balance(root.left_child) >= 0:
            return self.rotate_right(root)

        if balance_factor > 1 and self.get_balance(root.left_child) < 0:
            root.left_child = self.rotate_left(root.left_child)
            return self.rotate_right(root)

        if balance_factor < -1 and self.get_balance(root.right_child) <= 0:
            return self.rotate_left(root)

        if balance_factor < -1 and self.get_balance(root.right_child) > 0:
            root.right_child = self.rotate_right(root.right_child)
            return self.rotate_left(root)

        return root

    def search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self.search(root.left_child, value)
        return self.search(root.right_child, value)

    def find_min_node(self, node):
        if node is None or node.left_child is None:
            return node
        return self.find_min_node(node.left_child)

    def rotate_left(self, z):
        y = z.right_child
        T2 = y.left_child
        y.left_child = z
        z.right_child = T2
        z.node_height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.node_height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        return y

    def rotate_right(self, z):
        y = z.left_child
        T3 = y.right_child
        y.right_child = z
        z.left_child = T3
        z.node_height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.node_height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.node_height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left_child) - self.get_height(node.right_child)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left_child, result)
            result.append(node.value)
            self.inorder_traversal(node.right_child, result)
        return result


def avl_program():
    avl_tree = AVLTree()
    root_node = None
    while True:
        print("\nAVL Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. In-order Traversal")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to insert: "))
            root_node = avl_tree.insert(root_node, value)
            print(f"{value} inserted.")
        elif choice == 2:
            value = int(input("Enter value to delete: "))
            root_node = avl_tree.delete(root_node, value)
            print(f"{value} deleted.")
        elif choice == 3:
            value = int(input("Enter value to search: "))
            found_node = avl_tree.search(root_node, value)
            if found_node:
                print(f"{value} found in AVL Tree.")
            else:
                print(f"{value} not found in AVL Tree.")
        elif choice == 4:
            print("In-order Traversal:", avl_tree.inorder_traversal(root_node, []))
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

avl_program()
