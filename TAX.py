Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #THIS PROGRAM IS INTENDED TO AID IN THE CALCULATION OF TAX ON A GIVEN PURCHASE
... 
... def calculate_tax(purchase_amount):
...     tax_rate = 0.0  # Initialize tax rate to 0
... 
...     if purchase_amount < 50:
...         tax_rate = 0.05  # 5% tax for purchases under $50
...     elif purchase_amount < 100:
...         tax_rate = 0.07  # 7% tax for purchases between $50 and $100
...     elif purchase_amount < 200:
...         tax_rate = 0.08  # 8% tax for purchases between $100 and $200
...     else:
...         tax_rate = 0.10  # 10% tax for purchases over $200
... 
...     tax_amount = purchase_amount * tax_rate
...     return tax_amount
... 
... # Example usage
... purchase_amount = float(input("Enter the purchase amount: "))
... tax = calculate_tax(purchase_amount)
