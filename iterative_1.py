def get_item_cost():
  price = float(input("Enter the price: $"))
  return price

def calculate_sales_tax(price):
  sales_tax = price * 0.06625
  return sales_tax
  
def calculate_total_cost(price, sales_tax):
  total = price + sales_tax
  return total

def print_receipt(price, sales_tax, total):
  print(f"Price: {price}")
  print(f"Sales Tax: {sales_tax}")
  print(f"Total Cost: {total}")

price = get_item_cost()
tax = calculate_sales_tax(price)
total = calculate_total_cost(price, tax)
print_receipt(price, tax, total)









  

