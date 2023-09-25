class Cart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, cost):
        self.cart[item] = cost
    
    def remove_item(self, item):
        self.cart.pop(item)
      
    def total_cost(self):
        print(sum(self.cart.values()))

shoppingCart = Cart()
shoppingCart.add_item("soap", 10)
shoppingCart.add_item("bat", 20)
shoppingCart.add_item("cat", 30)
print(shoppingCart.cart)

shoppingCart.remove_item("bat")
print(shoppingCart.cart)

shoppingCart.total_cost()
