"""
=========================
Sorting Algorithms in Python
=========================

This file explains and implements 5 major sorting algorithms:
1. Selection Sort
2. Bubble Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort

Each section includes:
- Explanation
- Working steps
- Time and Space Complexity
- Example Python Implementation
"""

# =========================================================
# 🟡 1. Selection Sort
# =========================================================
"""
Idea:
Repeatedly find the minimum element from the unsorted part
and put it at the beginning.

Steps:
1. Loop through the list.
2. Find the smallest element in the unsorted section.
3. Swap it with the first unsorted element.

Time Complexity:
Best: O(n²)
Worst: O(n²)
Space: O(1)
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# =========================================================
# 🔵 2. Bubble Sort
# =========================================================
"""
Idea:
Repeatedly compare adjacent elements and swap if they are in the wrong order.

Steps:
1. Compare each pair of adjacent elements.
2. Swap if the left element is greater.
3. Each iteration “bubbles” the largest element to the end.

Time Complexity:
Best: O(n)
Worst: O(n²)
Space: O(1)
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# =========================================================
# 🟢 3. Insertion Sort
# =========================================================
"""
Idea:
Build the sorted list one element at a time by inserting
each new element into the correct position.

Steps:
1. Start from the 2nd element.
2. Compare with the elements before it.
3. Insert it into the correct place among the sorted elements.

Time Complexity:
Best: O(n)
Worst: O(n²)
Space: O(1)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# =========================================================
# 🔴 4. Merge Sort
# =========================================================
"""
Idea:
Divide and conquer — divide the array into halves,
sort each half, and then merge them.

Steps:
1. Divide the array until each subarray has one element.
2. Merge the sorted halves in order.

Time Complexity:
Best/Worst/Average: O(n log n)
Space: O(n)
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


# =========================================================
# 🟣 5. Quick Sort
# =========================================================
"""
Idea:
Divide and conquer — choose a pivot, partition the array so that
elements smaller than pivot go left, greater go right, then recursively sort the sides.

Steps:
1. Pick a pivot (e.g., last element).
2. Rearrange elements around the pivot.
3. Recursively sort the subarrays.

Time Complexity:
Best: O(n log n)
Worst: O(n²)
Space: O(log n)
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


# =========================================================
# 🧮 Testing the functions
# =========================================================
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original:", data)
    print("Selection Sort:", selection_sort(data.copy()))
    print("Bubble Sort:", bubble_sort(data.copy()))
    print("Insertion Sort:", insertion_sort(data.copy()))
    print("Merge Sort:", merge_sort(data.copy()))
    print("Quick Sort:", quick_sort(data.copy()))

"""
Summary Table:

| Algorithm       | Best Time | Worst Time | Space | Type           | Stable |
|-----------------|------------|-------------|--------|----------------|---------|
| Selection Sort  | O(n²)      | O(n²)       | O(1)   | In-place       | No  |
| Bubble Sort     | O(n)       | O(n²)       | O(1)   | In-place       | Yes |
| Insertion Sort  | O(n)       | O(n²)       | O(1)   | In-place       | Yes |
| Merge Sort      | O(n log n) | O(n log n)  | O(n)   | Divide-Conquer | Yes |
| Quick Sort      | O(n log n) | O(n²)       | O(log n) | Divide-Conquer | No |
"""
