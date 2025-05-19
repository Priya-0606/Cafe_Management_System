#Menu of cafe

Menu = {

    'COFFEE': 80,

    'AMERICANO': 80,

    'LATTE': 70,

    'COLD COFFEE': 75,

    'HOT COCOA': 90,

    'CAPPUCCINO': 100,

    'VANILLA LATTE': 120,

    'ESPRESSO': 150,

    'COLD MOCHA': 160,

    'FRAPPE': 110,

    'COCOA': 90,

}

# Greet
print("-------------------------------------------------")
print("-------------------------------------------------")

print(" *--------------**--------------**--------------*")

print("\n\t\tPython Coffee House! \n")
print("-------------------------------------------------")

print("\n\t\tWelcome to Our Cafe! \n")
print("-------------------------------------------------")

print("\n\t\t\tOur Menu \n")
print("-------------------------------------------------")

#print("\n",Menu)

print(" *--------------**--------------**--------------*")

for item, price in Menu.items():

    print(f"\t\t {item} : Rs {price}\n ")

print(" *--------------**--------------**--------------*")

print("-------------------------------------------------")


# Get customer information

Name = input("\nYour Name: ")

Cont = input("Your Contact: ")


# Initialize order total

order_total = 0

order_items ={}


# Get first order

I1 = input("\nEnter the name of the item you want to order: ").upper()

if I1 in Menu:

    quantity = int(input("Enter the quantity : "))

    order_total += Menu[I1]*quantity

    order_items[I1] = quantity

    print(f"Your item {I1} has been added to your order \n")

else:

    print(f"Ordered item {I1} is not available yet, So please order something else from menu \n")


# Ask if they need anything else
print("-------------------------------------------------")

while True:

    Another_order = input("Do you want to order something else? (Yes/No): ").upper()

    if Another_order == "YES":

        item = input("\nEnter the name of the item you want to order: ").upper()

        if item in Menu:

            quantity = int(input("Enter the quantity : "))

            order_total += Menu[item]*quantity

            order_items[item] = quantity

            print(f"Your item {item} has been added to your order \n")

        else:

            print(f"Sorry, {item} is not available in menu.")

    else:

        break
print("-------------------------------------------------")


print(f"Your total order is: Rs {order_total}\n")


# Get payment method


payment_method = input("Choose payment method (cash, card, online): ").upper()


# Calculate change due


if payment_method == "CASH":

    cash_paid = int(input("Enter cash paid: "))

    change_due = cash_paid - order_total

print("Change Due : {change_due}",change_due)
print("-------------------------------------------------")
    


# Offer discounts

if order_total >= 1000:

    discount = order_total * 0.10

    print(f"Discount applied: Rs {order_total * 0.10}")

    order_total = order_total - discount

    order_total -= discount

    change_due = cash_paid - order_total

# order summary

print(f"\nYour order summary is: \n")

for item, quantity in order_items.items():

    {

    print(f"{quantity}  {item} : Rs {Menu[item]*quantity} ")

    }
  
   
print("-------------------------------------------------")
    

print(f"\nName: {Name}")

print(f"Contact: {Cont}")


print(f"Your total Payable Amount is: Rs {order_total}\n")
print("-------------------------------------------------")

print("\nThank you for using our service!!\n")


print(" *--------------**--------------**--------------*")
print("-------------------------------------------------")



