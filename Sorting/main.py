def selection_sort(arr):
  n = len(arr)
  for i in range(n):
      min_index = i
      for j in range(i+1, n):
          if arr[j] < arr[min_index]:
              min_index = j
    

arr = [5, 2, 8, 3, 6, 1]
result = selection_sort(arr)
print(result)