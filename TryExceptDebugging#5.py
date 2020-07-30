'''
Compare the following programs below

'''

# program 1 without try and except

#Function to calculate discount and tax amount
def price_calculator(price, discount):
  # discount_rate=discount/100  if you just let the user enter a number and not a .something
  discount_amount = price * discount. # change discount to discount rate if the user only enters an integer not a decimal
  price= price - discount_amount
  return price

original_price = float(input("What is the total cost of the order? "))
discount = float(input("Enter discount %: "))
discounted_price = price_calculator(original_price, discount)
print("The discounted price is", discounted_price)

# same program #2 with try and except 

#Function to calculate discount and tax amount
def price_calculator(price, discount):
  discount_rate = discount / 100
  discount_amount = price * discount_rate
  price -= discount_amount
  return price

#Ask the user for the price
while True:
  try:
    original_price = float(input("What is the total cost of the order? "))
    break
  except ValueError:
    print("Please enter a valid number")

while True:
  try:
    discount = float(input("Enter discount %: "))
    if discount >= 0 and discount <= 100:
      break
    else:
      print("Please enter a value between 0 and 100")
  except ValueError:
    print("Please enter a valid number")
      
discounted_price = price_calculator(original_price, discount)

print("The price", discounted_price)


#################################################################





#################################################################





#################################################################
