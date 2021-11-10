#If the subtotal is $50 or greater and today is Tuesday or Wednesday,
# your program must subtract 10% from the subtotal. Your program must then
# compute the total amount due by adding sales tax of 6% to the subtotal.
# Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

import math

from datetime import datetime
date = datetime.now()
datetime.today().weekday()

sub_total = float(input("Please enter your subtotal: "))
discount = .10
sales_tax =.06
sales_tax_amount = sub_total * sales_tax

# If its a tuesday or wednesday and sub_total is over 50
def calculate_total():
    if datetime.now() == 1 or datetime.now() == 2:
        if sub_total >= 50:
            total = sub_total - (sub_total * discount) + sales_tax_amount
            discount_amount = sub_total * discount
            print(f"Sales tax amount: {sales_tax_amount:.2f}")
            print(f'Discount: {discount_amount}')
            print(f"Total: {total:.2f}")
# If its any other day or sub_total is below 50   
    else:
        total = sub_total + sales_tax_amount
        discount_amount = sub_total * discount
        
        print(f"Sales tax amount: {sales_tax_amount:.2f}")
        print(f"discount: {discount_amount:.2f}")  
        print(f"Total: {total:.2f}")
calculate_total()
