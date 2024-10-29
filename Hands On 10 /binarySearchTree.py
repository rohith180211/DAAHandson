class TreeNode:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value

class BSTree:
    def __init__(self):
        self.root_node = None

    def insert(self, value):
        if self.root_node is None:
            self.root_node = TreeNode(value)
        else:
            self._insert_helper(self.root_node, value)

    def _insert_helper(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(value)
            else:
                self._insert_helper(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(value)
            else:
                self._insert_helper(current_node.right_child, value)

    def search(self, value):
        found = self._search_helper(self.root_node, value)
        if found:
            print(f"{value} found in BST.")
        else:
            print(f"{value} not found in BST.")

    def _search_helper(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search_helper(current_node.left_child, value)
        return self._search_helper(current_node.right_child, value)

    def delete(self, value):
        if self.root_node is None:
            print(f"{value} not found in BST.")
            return self.root_node
        self.root_node, was_deleted = self._delete_helper(self.root_node, value)
        if was_deleted:
            print(f"{value} deleted.")
        else:
            print(f"{value} not found in BST.")

    def _delete_helper(self, current_node, value):
        if current_node is None:
            return current_node, False

        if value < current_node.value:
            current_node.left_child, was_deleted = self._delete_helper(current_node.left_child, value)
            return current_node, was_deleted
        elif value > current_node.value:
            current_node.right_child, was_deleted = self._delete_helper(current_node.right_child, value)
            return current_node, was_deleted

        if current_node.left_child is None:
            return current_node.right_child, True
        elif current_node.right_child is None:
            return current_node.left_child, True

        successor = self._find_min_node(current_node.right_child)
        current_node.value = successor.value
        current_node.right_child, _ = self._delete_helper(current_node.right_child, successor.value)
        return current_node, True

    def _find_min_node(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current

    def inorder_traversal(self):
        return self._inorder_helper(self.root_node, [])

    def _inorder_helper(self, node, traversal_result):
        if node:
            self._inorder_helper(node.left_child, traversal_result)
            traversal_result.append(node.value)
            self._inorder_helper(node.right_child, traversal_result)
        return traversal_result

def bst_program():
    bst = BSTree()
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. In-order Traversal")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to insert: "))
            bst.insert(value)
            print(f"{value} inserted.")
        elif choice == 2:
            value = int(input("Enter value to delete: "))
            bst.delete(value)
        elif choice == 3:
            value = int(input("Enter value to search: "))
            bst.search(value)
        elif choice == 4:
            print("In-order Traversal:", bst.inorder_traversal())
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

bst_program()
