class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add(self, key, data):
        new_node = Node(key, data)
        if not self.head_node:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next_node = new_node
            new_node.prev_node = self.tail_node
            self.tail_node = new_node

    def search(self, key):
        current = self.head_node
        while current:
            if current.key == key:
                return current
            current = current.next_node
        return None

    def delete(self, key):
        node_to_remove = self.search(key)
        if not node_to_remove:
            return

        if node_to_remove.prev_node:
            node_to_remove.prev_node.next_node = node_to_remove.next_node
        else:
            self.head_node = node_to_remove.next_node

        if node_to_remove.next_node:
            node_to_remove.next_node.prev_node = node_to_remove.prev_node
        else:
            self.tail_node = node_to_remove.prev_node

    def display(self):
        current = self.head_node
        while current:
            print(f"[{current.key}: {current.data}]", end=" ")
            current = current.next_node
        print()

class HashMap:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.current_size = 0
        self.max_load = 0.75
        self.min_load = 0.25
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]

    def _hash(self, key):
        fraction = (key * 0.618033) % 1
        index = int(self.capacity * fraction) % self.capacity
        return index

    def put(self, key, data):
        index = self._hash(key)
        node = self.buckets[index].search(key)

        if node:
            node.data = data
        else:
            self.buckets[index].add(key, data)
            self.current_size += 1

            if self.current_size / self.capacity > self.max_load:
                self._resize(self.capacity * 2)

    def get(self, key):
        index = self._hash(key)
        node = self.buckets[index].search(key)
        if node:
            return node.data
        else:
            raise KeyError("Key not found.")

    def remove(self, key):
        index = self._hash(key)
        self.buckets[index].delete(key)
        self.current_size -= 1

        if self.capacity > 4 and self.current_size / self.capacity < self.min_load:
            self._resize(self.capacity // 2)

    def _resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [DoublyLinkedList() for _ in range(new_capacity)]
        self.current_size = 0

        for bucket in old_buckets:
            current = bucket.head_node
            while current:
                self.put(current.key, current.data)
                current = current.next_node

    def display_table(self):
        for i in range(self.capacity):
            print(f"Bucket {i}: ", end="")
            self.buckets[i].display()

def main():
    hash_map = HashMap()
    while True:
        print("\nHash Map Operations:")
        print("1. Insert")
        print("2. Get Value")
        print("3. Delete")
        print("4. Display Table")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            hash_map.put(key, value)
            print(f"Added ({key}, {value})")

        elif choice == '2':
            key = int(input("Enter key to retrieve: "))
            try:
                value = hash_map.get(key)
                print(f"Value for key {key}: {value}")
            except KeyError:
                print("Key not found.")

        elif choice == '3':
            key = int(input("Enter key to delete: "))
            hash_map.remove(key)
            print(f"Key {key} removed.")

        elif choice == '4':
            print("Hash Map:")
            hash_map.display_table()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
