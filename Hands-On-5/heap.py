from typing import TypeVar

T = TypeVar('T')

class MinHeap:
    
    heap: list[T] = []
    
    # Constructor
    def __init__(self, elements: list[T]) -> None:
        self.heap = elements
    
    # Add a new element to the heap
    def add_element(self, value: T):
        # Append the new value at the end of the heap
        self.heap.append(value)
        
        # Index of the newly added element
        index = len(self.heap) - 1
        parent_index = (index - 1) >> 1
        
        # Restore the heap property by moving the new element up
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) >> 1

    def heapify_down(self, size: int, index: int):
        # Initial assumption: the smallest is the root
        smallest = index
        
        # Children indices (using bitwise operations)
        left_child = (index << 1) + 1         
        right_child = (index << 1) + 2

        # If the left child is smaller
        if left_child < size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        # If the right child is smaller
        if right_child < size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # If the smallest is not the root, swap and continue heapifying down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(size, smallest)

    def create_min_heap(self):
        size = len(self.heap)
        # Start from the last non-leaf node and heapify down
        for i in range(size // 2 - 1, -1, -1):
            self.heapify_down(size, i)
            
    def get_min(self) -> T:
        return self.heap[0] if self.heap else None
        
    def remove_min(self) -> T:
        if not self.heap:
            return None
        
        # Replace root with the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()  # Remove the last element
        
        # Restore heap property
        self.heapify_down(len(self.heap), 0)

if __name__ == '__main__':
    
    # --------------------------------------------------------------------------------------

    # BUILD MIN HEAP
    
    # Example 1
    initial_data = [40, 25, 35, 15, 20, 5, 30]
    min_heap = MinHeap(initial_data)
    min_heap.create_min_heap()    
    print(f'Min Heap: {min_heap.heap}\n')
    
    # Example 2
    initial_data = [3, 8, 2, 6, 1]
    min_heap = MinHeap(initial_data)
    min_heap.create_min_heap()
    print(f'Min Heap: {min_heap.heap}\n')

    # Example 3
    initial_data = [1, 2, 3, 4, 5]
    min_heap = MinHeap(initial_data)
    min_heap.create_min_heap()
    print(f'Min Heap: {min_heap.heap}\n')

    # Example 4
    initial_data = [9, 7, 5, 3, 2, 1]
    min_heap = MinHeap(initial_data)
    min_heap.create_min_heap()
    print(f'Min Heap: {min_heap.heap}\n')

    # Example 5
    initial_data = [6.5, 1.3, 4.2, 3.8, 0.9]
    min_heap = MinHeap(initial_data)
    min_heap.create_min_heap()
    print(f'Min Heap: {min_heap.heap}\n')

    # Example 6
    initial_data = [100, 80, 70, 60, 50, 40]
    min_heap = MinHeap(initial_data)
    min_heap.create_min_heap()
    print(f'Min Heap: {min_heap.heap}\n')

    # Example 7 (empty array)
    empty_heap = MinHeap([])
    empty_heap.create_min_heap()
    print(f'Min Heap: {empty_heap.heap}')
    
    # --------------------------------------------------------------------------------------
    
    # INSERT NEW ELEMENT IN HEAP
    min_heap = MinHeap([3, 6, 10, 8])
    min_heap.add_element(2)
    print("Heap after adding 2:", min_heap.heap)

    min_heap.add_element(5)
    print("Heap after adding 5:", min_heap.heap, "\n")
    
    # --------------------------------------------------------------------------------------
    
    # GET ROOT ELEMENT
    initial_data = [8, 5, 6, 2, 3, 4]
    print(f'Initial Array: {initial_data}')
    
    min_heap = MinHeap(initial_data)
    min_heap.create_min_heap()
    print(f'Heap created: {min_heap.heap}')
    print(f'Root element: {min_heap.get_min()}\n')
    
    # --------------------------------------------------------------------------------------
    
    # REMOVE ROOT ELEMENT 
    min_heap.remove_min()
    print(f'Heap after removing root: {min_heap.heap}\n')
