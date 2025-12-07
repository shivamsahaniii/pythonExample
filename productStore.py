class productStore:
    count = 0  #class attribute

    def __init__(self, name, price):  #instance attribute
        self.name = name
        self.price = price
        productStore.count += 1

    def get_info(self): #instance method
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod   #class method
    def get_count(cls):
        print(f"Total products in store = {cls.count}")

    @staticmethod  #static method
    def cal_discount(price, discount):
        total_price = price - (discount * price / 100)
        print(f"discounted price is: {total_price}")


p1 = productStore("phone", 30_000)
p2 = productStore("laptop", 80_000)
p3 = productStore("smartWatch", 20_000)

p1.cal_discount(p1.price, 12)