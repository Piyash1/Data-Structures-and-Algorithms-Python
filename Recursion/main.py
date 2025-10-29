#Print GFG n times using Recursion

def printGFG(n):
    if n == 0:
        return
    print("GFG", end = ' ')
    printGFG(n-1)

#Example Usage
n = int(input("Enter a number: "))
printGFG(n)