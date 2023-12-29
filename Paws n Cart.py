"""Pet Shopping Cart Program:

This Python program simulates a simple pet shopping cart system. It consists of two classes:
- PetProduct: Represents a pet product with attributes such as name, price, and quantity.
- ShoppingCart: Represents a shopping cart that allows users to add, remove, and view pet products."""

# Define a class to represent a pet product
class PetProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 1

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity}) - £{self.price:.2f}"

# Define a class to represent a shopping cart
class ShoppingCart:
    def __init__(self):
        self.cart = []    # List to store products in the cart
        self.prices = []  # List to store prices for each product in the cart

    def add_to_cart(self, product, quantity):
        # Check if the product is already in the cart
        item = next((item for item in self.cart if item.name == product.name), None)
        if item:
            # If the product is in the cart, update the quantity
            item.quantity += quantity
            print(f"Added {quantity} more '{product.name}' to your cart.")
        else:
            # If the product is not in the cart, add it
            product.quantity = quantity
            self.cart.append(product)
            print(f"Added {quantity} {product.name} to your cart.")
            self.prices.extend([product.price] * quantity)

    def remove_from_cart(self, product_name, quantity_to_remove=None):
        # Find the product in the cart based on the product name
        product = next((item for item in self.cart if item.name.lower() == product_name.lower()), None)
        if product:
            # If a specific quantity is provided, remove that quantity; otherwise, remove all
            if quantity_to_remove is None or quantity_to_remove >= product.quantity:
                self.cart.remove(product)
                self.prices.remove(product.price * product.quantity)
                print(f"Removed all '{product.name}' from your cart.")
            else:
                product.quantity -= quantity_to_remove
                print(f"Removed {quantity_to_remove} '{product.name}' from your cart.")
        else:
            print(f"'{product_name}' not found in your cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nYour Shopping Cart:")
            # Calculate the total cost and display each product in the cart
            total_cost = sum(product.price * product.quantity for product in self.cart)
            for product in self.cart:
                print(product)
            print(f"\nTotal cost: £{total_cost:.2f}")

    def display_available_products(self):
        print("\nAvailable Products:")
        # Define available products using a dictionary
        products = {
            "1": PetProduct("Dog Food", 20.99),
            "2": PetProduct("Cat Toy", 8.50),
            "3": PetProduct("Bird Cage", 35.75),
        }
        # Display available products with corresponding keys
        for key, product in products.items():
            print(f"{key}. {product.name} - £{product.price:.2f}")
        return products

# Sample Usage
cart = ShoppingCart()

while True:
    print("\nMenu:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout and exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Allow the user to add items to the cart
        cart.display_available_products()
        product_choice = input("Enter the number of the product you want to add to your cart: ")
        if product_choice in {"1", "2", "3"}:
            try:
                quantity = int(input(f"Enter the quantity for {cart.display_available_products()[
                    product_choice].name}: "))
                cart.add_to_cart(cart.display_available_products()[product_choice], quantity)
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
        else:
            print("Invalid product choice. Please enter a number between 1 and 3.")

    elif choice == "2":
        # Allow the user to remove items from the cart
        product_name = input("Enter the name of the product to remove: ").lower()
        product_in_cart = next((product for product in cart.cart if product.name.lower() == product_name.lower()), None)
        if product_in_cart:
            if product_in_cart.quantity > 1:
                print(f"There are {product_in_cart.quantity} '{product_in_cart.name}' in your cart.")
                try:
                    remove_option = input("Do you want to remove 1 (Enter '1'), all ("
                                          "Enter 'all'), or enter a specific number?: ")
                    if remove_option.lower() == "all":
                        cart.remove_from_cart(product_name)
                    elif remove_option.isdigit():
                        quantity_to_remove = int(remove_option)
                        cart.remove_from_cart(product_name, quantity_to_remove)
                    else:
                        print("Invalid input. No items removed.")
                except ValueError:
                    print("Invalid input. No items removed.")
            else:
                cart.remove_from_cart(product_name)
        else:
            print(f"'{product_name}' not found in your cart.")

    elif choice == "3":
        # Display the contents of the cart
        cart.view_cart()

    elif choice == "4":
        # Checkout and exit the program
        print(f"\nThank you for shopping with Paws n Cart!")
        break

    else:
        # Handle invalid choices
        print("Invalid choice.")
