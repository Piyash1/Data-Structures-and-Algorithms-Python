def isMinHeap(arr):
    n = len(arr)
    
    # Only need to check all internal nodes (parents)
    for i in range((n // 2)):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # If left child exists and violates min-heap property
        if left < n and arr[i] > arr[left]:
            return False
        
        # If right child exists and violates min-heap property
        if right < n and arr[i] > arr[right]:
            return False
    
    return True

# Example usage
if __name__ == "__main__":
    arr1 = [1, 3, 2, 7, 6, 4, 5]
    arr2 = [1, 2, 3, 4, 5, 6, 0]
    
    print("Array 1 is min-heap:", isMinHeap(arr1))  # Expected: True
    print("Array 2 is min-heap:", isMinHeap(arr2))  # Expected: False