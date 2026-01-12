class FoodOrder:
    def __init__(self, customer_name, restaurant_name, category, prices):
        self.customer_name = customer_name
        self.restaurant_name = restaurant_name
        self.category = category
        self.prices = prices
    def average_price(self):
        return sum(self.prices) / len(self.prices)
    def order_type(self):
        avg = self.average_price()
        if avg >= 500:
            return "Premium Order"
        elif 350 <= avg <= 499:
            return "Gold Order"
        elif 200 <= avg <= 349:
            return "Silver Order"
        elif 100 <= avg <= 199:
            return "Regular Order"
        else:
            return "Basic Order"
if __name__ == "__main__":
    order = FoodOrder(
        customer_name="Sanjeev",
        restaurant_name="Food Hub",
        category="Fast Food",
        prices=[250, 300, 350]
    )
    print("Customer Name:", order.customer_name)
    print("Restaurant Name:", order.restaurant_name)
    print("Food Category:", order.category)
    print("Average Price:", order.average_price())
    print("Order Category:", order.order_type())
