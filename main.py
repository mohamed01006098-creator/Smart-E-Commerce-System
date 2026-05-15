class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.__price = price 

   
    def get_price(self):
        return self.__price

    def set_price(self, new_price):
      
            self.__price = new_price


    def apply_discount(self):
        return self.__price

    def display_info(self):
        print(f"ID: {self.product_id} | {self.name} | Price: ${self.__price}")



class DigitalProduct(Product):
    def __init__(self, product_id, name, price, link):
        super().__init__(product_id, name, price)
        self.link = link

    
    def apply_discount(self):
        return self.get_price() * 0.8   

    def display_info(self):
        print(f"ID: {self.product_id} | {self.name} | Price: ${self.get_price()} | Digital")


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, weight):
        super().__init__(product_id, name, price)
        self.weight = weight


    def apply_discount(self):
        return self.get_price() * 0.9  

    def display_info(self):
        print(f"ID: {self.product_id} | {self.name} | Price: ${self.get_price()} | Weight: {self.weight}kg")


class ShoppingCart:
    def __init__(self):
        self.moh = []

    def add_item(self, product):
        self.moh.append(product)
        print(f"{product.name} added to cart!")

    def checkout(self):
        total = 0

       

        for x in self.moh:
            final_price = x.apply_discount()

            print(f"{x.name} cash: ${final_price}")

            total += final_price

        print(f"Total = ${total}")



p1 = PhysicalProduct(1, "Laptop", 1000, 2.5)
p2 = PhysicalProduct(2, "Mouse", 50, 0.2)
p3 = DigitalProduct(3, "Python Course", 100, "course.com")


cart = ShoppingCart()

while True:
    print("1. View Products")
    print("2. Add Product")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        p1.display_info()
        p2.display_info()
        p3.display_info()

    elif choice == "2":
        pid = int(input("Enter Product ID: "))

        if pid == 1:
            cart.add_item(p1)

        elif pid == 2:
            cart.add_item(p2)

        elif pid == 3:
            cart.add_item(p3)

        else:
            print("Product not found!")

    elif choice == "3":
        cart.checkout()

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice!")