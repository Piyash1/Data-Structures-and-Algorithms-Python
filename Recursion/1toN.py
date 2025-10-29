#Print 1 to N using Recursion

class Solution:    
    def printNos(self,n):
        if  n == 0:
            return
        self.printNos(n-1)
        print(n, end = ' ')

#Example Usage
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    ob = Solution()
    ob.printNos(n)