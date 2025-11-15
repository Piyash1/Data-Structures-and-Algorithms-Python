def heapify(arr, index):
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
        heapify(arr, largest_index)

def array_to_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, i)
    return arr

# Example usage
if __name__ == "__main__":
    arr = [38, 58, 27, 68, 35, 52, 40, 18]
    print("Original array:", arr)
    heap = array_to_heap(arr)
    print("Array converted to max-heap:", heap)