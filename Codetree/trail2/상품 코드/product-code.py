product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product():
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code
    def __str__(self):
        return f'product {self.code} is {self.name}'

obj1 = Product()
obj2 = Product(product_name, product_code)

print(obj1)
print(obj2)