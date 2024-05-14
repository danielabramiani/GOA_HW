from typing import List 
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int
    
    def __str__(self):
        return f"{self.name} - ${self.price} - Quantity: {self.quantity}"
    
    
class ShoppingCart:
    def __init__(self):
        self.items: List[tuple] = []
        
    def add_item(self, product: Product, quantity: int):
        self.items.append((product, quantity))
        print(f"{quantity} {product.name}(s) added to cart.")
        
    def remove_item(self, product: Product, quantity: int):
        for item in self.items:
            if item[0] == product:
                if quantity >= item[1]:
                    self.items.remove(item)
                    print(f"All {product.name}(s) removed from cart.")
                else:
                    item[1] -= quantity
                    print(f"{quantity} {product.name}(s) removed from cart.")
                return
            print(f"{product.name} not found in cart.")
            
        def total(self) -> float:
            return sum(product.price * quantity for product, quantity in self.items)
        
        def __str__(self) -> str:
            if not self.items:
                return "Your cart is empty."
            cart_items = "\n".join([f"{product.name} - Quantity: {quantity}" for product, quantity in self.items])
            return f"items in your cart:\n{cart_items}\nTotal: ${self.total()}"
        
        
class OnlineShoppinSystem:
    def __init__(self):
        self.products: List[Product] = []
        
    def add_product(self)