class Solution():
    def heapify(self, arr, index, val):
        if arr[index] > val:
            arr[index] = val
            self.heapifyDown(arr, index)
        else:
            arr[index] = val
            self.heapifyUp(arr, index)
    
    def heapifyDown(self, arr, index):
        n = len(arr)
        largest_index = index
        
        leftchild_index = 2 * index + 1
        rightchild_index = 2 * index + 2
        
        if leftchild_index < n and arr[leftchild_index] > arr[largest_index]:
            largest_index = leftchild_index
        if rightchild_index < n and arr[rightchild_index] > arr[largest_index]:
            largest_index = rightchild_index
        
        if largest_index != index:
            arr[largest_index], arr[index] = arr[index], arr[largest_index]
            self.heapifyDown(arr, largest_index)

    def heapifyUp(self, arr, index):
        parent_index = (index - 1) // 2
        
        if index > 0 and arr[index] > arr[parent_index]:
            arr[index], arr[parent_index] = arr[parent_index], arr[index]
            self.heapifyUp(arr, parent_index)
            
# Example usage
if __name__ == "__main__":
    sol = Solution()
    arr = [50, 30, 40, 10, 20, 35, 25]
    print("Original heap:", arr)
    
    sol.heapify(arr, 1, 5)
    print("After updating index 1 to 5:", arr)
    
    sol.heapify(arr, 4, 60)
    print("After updating index 4 to 60:", arr)