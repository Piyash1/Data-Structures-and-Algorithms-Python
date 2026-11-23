# 1352. Product of the Last K Numbers

class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        
        else:
            product = self.prefix[-1] * num
            self.prefix.append(product)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        
        return self.prefix[-1] // self.prefix[-k-1]


# Example usage
obj = ProductOfNumbers()

obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)

print(obj.getProduct(2)) # 20
print(obj.getProduct(3)) # 40
print(obj.getProduct(4)) # 0

