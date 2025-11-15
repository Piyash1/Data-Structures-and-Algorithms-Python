class Solution():
    def __init__(self):
        self.arr = []
        self.count = 0
    
    def heapify_up(self, arr, index):
        parent_index = (index - 1) // 2
        
        if index > 0 and arr[index] < arr[parent_index]:
            arr[index], arr[parent_index] = arr[parent_index], arr[index]
            self.heapify_up(arr, parent_index)
    
    def heapify_down(self, arr, index):
        n = len(arr)
        smallest_index = index
        
        leftchild_index = 2 * index + 1
        rightchild_index = 2 * index + 2
        
        if leftchild_index < n and arr[leftchild_index] < arr[smallest_index]:
            smallest_index = leftchild_index
        if rightchild_index < n and arr[rightchild_index] < arr[smallest_index]:
            smallest_index = rightchild_index
        
        if smallest_index != index:
            arr[smallest_index], arr[index] = arr[index], arr[smallest_index]
            self.heapify_down(arr, smallest_index)
    
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

        if new_val < old_val:
            self.heapify_up(self.arr, index)
        else:
            self.heapify_down(self.arr, index)
    
    def extractMin(self):
        if self.count == 0:
            return None

        min_val = self.arr[0]
        self.arr[0] = self.arr[self.count - 1]
        self.arr.pop()
        self.count -= 1

        if self.count > 0:
            self.heapify_down(self.arr, 0)

        return min_val
    
    def isEmpty(self):
        return self.count == 0
    
    def getMin(self):
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
    
    print(f"Minimum value: {heap.getMin()}")
    print(f"Heap size: {heap.heapSize()}")
    print(f"Is heap empty? {heap.isEmpty()}")
    
    print("Extracting minimum values:")
    heap.extractMin()
    
    print("Changing key at index 1 to 2")
    heap.changeKey(1, 2)
    
    print(f"Minimum value after changes: {heap.getMin()}")
    
if __name__ == "__main__":
    main()