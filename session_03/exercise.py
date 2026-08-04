from functools import reduce

#داده اولیه
customers = ["Ali", "Sara", "Reza", "Nima"]
drinks = ["Coffee", "Tea", "Juice", "Latte"]
prices = [80, 40, 60, 120]
counts = [2, 1, 3, 1]

#1
orders = []

for customer, drink, price, count in zip(customers, drinks, prices, counts):
    order = {
        "customer": customer,
        "drink": drink,
        "price": price,
        "count": count
    }
    orders.append(order)

#2
print("Orders:")
for order in orders:
    print(f"{order['customer']} ordered {order['count']} {order['drink']}")

#3
print("Order Numbers:")
for i in range(len(orders)):
    print(f"Order {i + 1}")

#4
for order in orders:
    order["total"] = order["price"] * order["count"]

print("Orders with Total:")
for order in orders:
    print(order)

#5
total_sale = reduce(lambda x, y: x + y["total"], orders, 0)

print(f"Today's Sale: {total_sale}")