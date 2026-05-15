# Simple E-Commerce Shopping Cart

## Overview
This is a simple Python console-based shopping cart system using Object-Oriented Programming (OOP).

The program allows users to:
- View products
- Add products to a shopping cart
- Apply discounts
- Checkout and calculate the total price

---

# Features

## Product Management
- Base `Product` class
- Encapsulation using private price attribute (`__price`)
- Getter and setter methods for price

## Digital Products
- Represent online products like courses
- 20% discount applied automatically

## Physical Products
- Represent real items with weight
- 10% discount applied automatically

## Shopping Cart
- Add products to cart
- Display final discounted prices
- Calculate total checkout amount

## Menu System
Interactive console menu with:
1. View Products  
2. Add Product  
3. Checkout  
4. Exit

---

# Technologies Used
- Python
- Object-Oriented Programming (OOP)

---

# How to Run

## Step 1: Save the File
Save the code in a file named:

```bash
shopping_cart.py
```

## Step 2: Run the Program

Open terminal or command prompt and run:

```bash
python shopping_cart.py
```

---

# Example Output

```text
1. View Products
2. Add Product
3. Checkout
4. Exit

Choose: 1

ID: 1 | Laptop | Price: $1000 | Weight: 2.5kg
ID: 2 | Mouse | Price: $50 | Weight: 0.2kg
ID: 3 | Python Course | Price: $100 | Digital
```

---

# Discounts

| Product Type | Discount |
|---|---|
| Digital Product | 20% |
| Physical Product | 10% |

---

# OOP Concepts Used

- Classes and Objects
- Inheritance
- Polymorphism
- Encapsulation
- Method Overriding

---

# Author
Simple educational project for learning Python OOP concepts.
