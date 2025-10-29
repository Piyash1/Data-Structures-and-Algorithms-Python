# Frequencies in a limited array

# You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

def count_frequency(arr):
    n = len(arr)
    freq = [0] * (n + 1)  # 1-based indexing
    
    for num in arr:
        if 1 <= num <= n:  # Safety check (though problem guarantees 1 to n)
            freq[num] += 1
    
    return freq[1:]

# Example usage
arr = [2, 3, 2, 3, 5]
result = count_frequency(arr)
print(result) 