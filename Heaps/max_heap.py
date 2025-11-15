class Solution():
    def __init__(self):
        self.arr = []
        self.count = 0
    
    def heapify_up(self, arr, index):
        parent_index = (index - 1) // 2
        
        # Swap if child is greater than parent (Max Heap)
        if index > 0 and arr[index] > arr[parent_index]:
            arr[index], arr[parent_index] = arr[parent_index], arr[index]
            self.heapify_up(arr, parent_index)
    
    def heapify_down(self, arr, index):
        n = len(arr)
        largest_index = index
        
        leftchild_index = 2 * index + 1
        rightchild_index = 2 * index + 2
        
        # Compare left child
        if leftchild_index < n and arr[leftchild_index] > arr[largest_index]:
            largest_index = leftchild_index
        
        # Compare right child
        if rightchild_index < n and arr[rightchild_index] > arr[largest_index]:
            largest_index = rightchild_index
        
        # If a child is bigger, swap
        if largest_index != index:
            arr[largest_index], arr[index] = arr[index], arr[largest_index]
            self.heapify_down(arr, largest_index)
    
    def initializeHeap(self):
        self.arr.clear()
        self.count = 0
    
    def insert(self, val):
        self.arr.append(val)
        self.count += 1
        self.heapify_up(self.arr, self.count - 1)
    
    def changeKey(self, index, new_val):
        old_val = self.arr[index]
        self.arr[index] = new_val

        # If value increased → bubble UP
        if new_val > old_val:
            self.heapify_up(self.arr, index)

        # If value decreased → bubble DOWN
        else:
            self.heapify_down(self.arr, index)
    
    def extractMax(self):
        if self.count == 0:
            return None

        max_val = self.arr[0]
        self.arr[0] = self.arr[self.count - 1]
        self.arr.pop()
        self.count -= 1

        if self.count > 0:
            self.heapify_down(self.arr, 0)

        return max_val
    
    def isEmpty(self):
        return self.count == 0
    
    def getMax(self):
        if self.count == 0:
            return None
        return self.arr[0]
    
    def heapSize(self):
        return self.count

def main():
    heap = Solution()
    heap.initializeHeap()
    
    heap.insert(4)
    print("Inserted 4")
    heap.insert(5)
    print("Inserted 5")
    heap.insert(10)
    print("Inserted 10")
    
    print(f"Maximum value: {heap.getMax()}")
    print(f"Heap size: {heap.heapSize()}")
    print(f"Is heap empty? {heap.isEmpty()}")
    
    print("Extracting maximum value:")
    heap.extractMax()
    
    print("Changing key at index 1 to 20")
    heap.changeKey(1, 20)
    
    print(f"Maximum value after changes: {heap.getMax()}")
    
if __name__ == "__main__":
    main()
