class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1  # access class attributes

    def get_info(self):
        print(f"price of {self.name} is {self.price} taka")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def calculate_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"final price is = {final_price}")


product1 = Product("Pen", 20)
product2 = Product("Phone", 10_000)

product1.get_info()
product2.get_info()

Product.get_count()

product2.calculate_discount(product2.price, 12)
