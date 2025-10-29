def count_digits(n):
    """Count the number of digits in a non-negative integer n."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

# Example usage:
if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))
    print(f"The number of digits in {number} is {count_digits(number)}.")