#If the subtotal is $50 or greater and today is Tuesday or Wednesday,
# your program must subtract 10% from the subtotal. Your program must then
# compute the total amount due by adding sales tax of 6% to the subtotal.
# Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

from datetime import datetime


sub_total = float(input("Please type in your sub total: "))
discount = .10
tax = .06
current_date = datetime.now().weekday()

if sub_total >= 50 and (current_date == 1 or current_date == 3):
    discountNum = sub_total * discount
    print(f"Discount amount: {discountNum:.2f}")
    sub_total -= discountNum

sales_tax = sub_total * tax
print(f"Sales tax amount: {sales_tax:.2f}")

total = sub_total + sales_tax

print(f"Total: {total:.2f}")