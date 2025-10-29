# Check the given string is palindrome or not using recursion

class Solution:
    def isPalindrome(self, s, left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.isPalindrome(s, left + 1, right - 1)

# Example Usage
if __name__ == "__main__":
    s = input("Enter a string: ")
    ob = Solution()
    if ob.isPalindrome(s, 0, len(s) - 1):
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')