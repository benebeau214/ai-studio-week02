### 질문 내용

```python
# 기존 코드
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
        self.customer.add_points(price) 

```

‘Order: 속성: order_id, customer(Customer 인스턴스 참조), items((상품명, 가격) 튜플의 리스트) · 메서드: total_price() — 고객 등급 할인 적용 총액 반환 / add_item(name, price) — 상품 추가 · 결제 완료 시 customer.add_points()가 호출되도록 pay() 메서드를 설계’

이게 과제 명세인데 'add_item(name, price) — 상품 추가 · 결제 완료 시 customer.add_points()가 호출되도록 pay() 메서드를 설계'라는 게 무슨 뜻이야? 지금 내가 짠 코드가 조건을 만족해?

### AI 답변

“`pay()` 메서드를 설계”한다는 뜻은 결제 시점에 호출할 메서드를 직접 만들라는 의미입니다. 그리고 포인트 적립은 상품을 장바구니에 추가할 때가 아니라 **결제가 완료될 때** 실행되어야 합니다.

현재는 `add_item()`에서 이미 포인트가 적립됩니다.

따라서 다음처럼 수정하는 것이 명세에 맞습니다.

```python
class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.paid = False

    def total_price(self):
        subtotal = sum(price for _, price in self.items)
        discount = self.customer.get_discount_rate()
        return int(subtotal * (1 - discount))

    def add_item(self, name, price):
        self.items.append((name, price))

    def pay(self):
        if self.paid:
            return self.total_price()

        amount = self.total_price()
        self.customer.add_points(amount)
        self.paid = True
        return amount
```

`paid` 상태를 둔 이유는 `pay()`가 두 번 호출되어 포인트가 중복 적립되는 것을 방지하기 위해서입니다. 따라서 현재 코드는 `pay()`를 추가하고, `add_item()`의 포인트 적립을 `pay()`로 옮겨야 과제 조건을 정확히 만족합니다.

### AI 답변 채택 내용

‘상품 추가 · 결제 완료 시 customer.add_points()가 호출되도록 pay() 메서드를 설계’라는 문구에서 상품 추가 뒤에 문구도 add_item(name, price) 메서드의 요구조건인 줄 착각했으나 ai 답변을 통해 아닌 걸 알고 add_item() 메서드와 pay() 메서드를 따로 구분해서 작성했다.

다만 ai 답변에서 나온 포인트 중복 적립을 방지하는 paid flag 같은 경우는 이번 과제에서 동일 주문으로 포인트가 여러 번 적립되는 시나리오는 취급하지 않기 때문에 채택하지 않았다.