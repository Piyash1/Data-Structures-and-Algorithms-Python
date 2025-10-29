#Print N to 1 using Recursion

class Solution:    
    def printNos(self,n):
        if  n == 0:
            return
        print(n, end = ' ')
        self.printNos(n-1)

#Example Usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    ob = Solution()
    ob.printNos(n)