Pet Shopping Cart Program
This Python program simulates a simple pet shopping cart system. It consists of two classes:

PetProduct: Represents a pet product with attributes such as name, price, and quantity.
ShoppingCart: Represents a shopping cart that allows users to add, remove, and view pet products.
PetProduct Class
python
Copy code
class PetProduct:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.quantity = 1

  def __str__(self):
    return f"{self.name} (Quantity: {self.quantity}) - £{self.price:.2f}"
ShoppingCart Class
python
Copy code
class ShoppingCart:
  def __init__(self):
    self.cart = []    # List to store products in the cart
    self.prices = []  # List to store prices for each product in the cart

  def add_to_cart(self, product, quantity):
    # Check if the product is already in the cart
    # ... (see original code for implementation)

  def remove_from_cart(self, product_name, quantity_to_remove=None):
    # Find the product in the cart based on the product name
    # ... (see original code for implementation)

  def view_cart(self):
    # Display the contents of the cart
    # ... (see original code for implementation)

  def display_available_products(self):
    # Display available products and return a dictionary
    # ... (see original code for implementation)
Sample Usage
python
Copy code
# Sample usage of the program
cart = ShoppingCart()

while True:
  # Display menu and prompt user for input
  # ... (see original code for implementation)
Menu Options:
Add item to cart: Allows the user to add items to the cart.
Remove item from cart: Allows the user to remove items from the cart.
View cart: Displays the contents of the cart.
Checkout and exit: Completes the shopping process and exits the program.
Note: Ensure to enter valid choices and quantities when prompted.

Thank you for shopping with Paws n Cart!
