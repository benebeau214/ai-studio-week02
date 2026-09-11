class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        self.points += int(amount * 0.05)

    def get_discount_rate(self):
        if self.grade == "vip":
            return 0.10
        return 0.03

    def summary(self):
        return f"[{self.grade}] {self.name} (포인트: {self.points})"

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def total_price(self):
        subtotal = sum(price for _, price in self.items)
        discount = self.customer.get_discount_rate()
        return int(subtotal * (1 - discount))

    def add_item(self, name, price):
        self.items.append((name, price))

    def pay(self):
        amount = self.total_price()
        self.customer.add_points(amount)
        return amount


c1 = Customer("김리나", "vip")
c2 = Customer("박성현", "basic")

o1 = Order("A-001", c1, [("딸기 마카롱", 3500), ("망고 스무디", 5000)])
o1.pay()
print(f"주문 총액 : {o1.total_price()}원, {c1.summary()}")
o2 = Order("A-002", c2, [("바닐라 라떼", 4000), ("소금빵", 5500)])
o2.pay()
print(f"주문 총액 : {o2.total_price()}원, {c2.summary()}")
o3 = Order("A-003", c1, [("그릭 요거트", 7000)])
o3.pay()
print(f"주문 총액 : {o3.total_price()}원, {c1.summary()}")