from online_delivery import FoodOrder

def test_premium_order():
    order = FoodOrder("A", "R", "C", [600, 550, 500])
    assert order.order_type() == "Premium Order"

def test_gold_order():
    order = FoodOrder("A", "R", "C", [400, 350, 450])
    assert order.order_type() == "Gold Order"

def test_silver_order():
    order = FoodOrder("A", "R", "C", [250, 300, 200])
    assert order.order_type() == "Silver Order"

def test_regular_order():
    order = FoodOrder("A", "R", "C", [150, 180, 120])
    assert order.order_type() == "Regular Order"

def test_basic_order():
    order = FoodOrder("A", "R", "C", [50, 80, 90])
    assert order.order_type() == "Basic Order"
