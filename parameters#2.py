'''
Setting parameters for a function
Now that we have put the code for the area and perimeter functions together in one program, there is some repeated code. It would be useful if we only had to ask for the measurements once, and then we could tell the user both calculations using the same measurements. That's what parameters are for!

To set parameters for a function, we simply put the names that we want to refer to them as inside the brackets:

def my_function(a_parameter, another_parameter):
   #code that does stuff
You can have 0 or more parameters in a function. In this case, we want 2. Let's modify the code so that the functions take parameters.

'''

#Create a function that does an area calculation

def calc_area():
  length = float(input("What is the length of the rectangle in cm? "))
  width = float(input("What is the width of the rectangle in cm? "))
  area = length * width
  print("The area is:", area)

#Create a perimeter function for a rectangle
def calc_perimeter():
  length = float(input("What is the length of the rectangle in cm? "))
  width = float(input("What is the width of the rectangle in cm? "))
  perimeter = 2 *length + 2 * width
  print("The perimeter is: ",perimeter)

# WHAT PARTS REPEAT? what can we do about it? - enter params and reduce the lines of code.

# final draft
#Get the measurements from the user
#Create a function that does an area calculation
def calc_area(length, width):
  area = length * width
  print("The area is: {}cm".format(area))
#Create a perimeter function for a rectangle
def calc_perimeter(length, width):
  perimeter = 2 *length + 2 * width
  print("The area is: {}cm".format(perimeter))
#Get the measurements from the user
length = float(input("What is the length of the rectangle in cm? "))
width = float(input("What is the width of the rectangle in cm? "))

#################################################################################################
'''
FOLLOW UP
Using global variables.
Now that we have moved our variables outside of our functions, they have a global scope, 
and we should be able to access the values in the main part of our code.

Let's test that out before we use our functions.
'''

#Get the measurements from the user
#Create a function that does an area calculation
def calc_area(length, width):
  area = length * width
  print("The area is: {}cm".format(area))
#Create a perimeter function for a rectangle
def calc_perimeter(length, width):
  perimeter = 2 *length + 2 * width
  print("The area is: {}cm".format(perimeter))
#Get the measurements from the user
length = float(input("What is the length of the rectangle in cm? "))
width = float(input("What is the width of the rectangle in cm? "))

# print the width and length- they are global variables so there is no error. 
# print them just for testing
print(length)
print(width)

#################################################################################################
'''
Calling a function using arguments.
When we call a function that has parameters, we need to pass in the exact same number of values as we have set when we created the function. 
The values we pass into the function when we call it are called arguments, although the names argument and parameter are often seen being used for either.
Note that these values don't have to have the same names, although in this example they do because we're storing the user's input in length and width.
'''

# same code as above
def calc_area(length, width):
  area = length * width
  print("The area is: {}cm".format(area))
#Create a perimeter function for a rectangle
def calc_perimeter(length, width):
  perimeter = 2 *length + 2 * width
  print("The area is: {}cm".format(perimeter))
#Get the measurements from the user
length = float(input("What is the length of the rectangle in cm? "))
width = float(input("What is the width of the rectangle in cm? "))

calc_area(length,width)
calc_perimeter(length,width)
#################################################################################################
'''
Using return to get a value from a function
Parameters/arguments let us send values to a function, but sometimes a function needs to give us a value back so that we can use it. 
We use the return keyword to do this, which we have seen a couple of times already.

'''
# Task: fix the function to work correctly

#A function that adds 100 to a number
def add_100(number):
  number ??? 100
  return number
  
#A function that multiplies a string
def multiply_string(string, number):
  new_string = string * number
  # return the string
  

#Call the functions FINAL

#A function that adds 100 to a number
def add_100(number):
  number=number + 100
  return number
  
#A function that multiplies a string
def multiply_string(string, number):
  new_string = string * number
  return new_string
  

#Call the functions
print(add_100(5))
print(multiply_string("Hello",3))
#################################################################################################
'''
Storing returned values to use in the program
So if a value gets returned by a function, we can print it to see it, but that's not really that useful. 
Chances are we'll want to use the value for something else in our program, so it makes sense to store it in a variable.

To do this, we just use our usual = operator to assign a value, and in this case we put the call on the right hand side:

new_number = add_100(5)
Then we can access the returned value by using the variable name new_number.

'''
# DRAFT FOR STUDENTS 

#This function calculates the price after a discount and returns it. It takes 2 parameters: price and discount.
def calc_discount(price, discount):
  #Turn the discount % into a decimal
  discount_value = discount / 100 
  
  #Calculate the amount to discount and take off price
  discount_amount = price ??? discount_value
  price ??? discount_amount
  
  return ???
  
#Calculate the discount on a price and tell the user


print("The new price after the discount is:", new_prince)


# FINAL PROGRAM 
#This function calculates the price after a discount and returns it. It takes 2 parameters: price and discount.
def calc_discount(price, discount):
  #Turn the discount % into a decimal
  #discount_value = discount / 100 
  
  #Calculate the amount to discount and take off price
  discount_amount = price * discount
  price = price- discount_amount
  return price
  
#Calculate the discount on a price and tell the user
new_price = calc_discount(39.99, .15)

print("The new price after the discount is: $",new_price)

#################################################################################################
'''
Using variables as arguments and getting returned values.
Alright, so we've seen a good example of a function with one job that returns a value for us to use.

Let's refactor our code and make it a bit more flexible and robust now. 
We're going to ask the user for the price and discount, and we're going to make sure they enter numbers.
'''


#This function calculates the price after a discount and returns it. It takes 2 parameters: price and discount.
def calc_discount(price, discount):
  #Turn the discount % into a decimal
  #discount_value = discount / 100 
  
  #Calculate the amount to discount and take off price
  discount_amount = price * discount
  price = price- discount_amount
  return price
  
#Calculate the discount on a price and tell the user
new_price = calc_discount(39.99, .15)

print("The new price after the discount is: $",new_price)
#################################################################################################
#FUNCTION THAT FORCES A NUMERIC INPUT
#discount program

# Function to force numeric input
def force_number(message):
  while True:
    try:
      number = float(input(message))
      break
    except ValueError:
      print("Please enter a number!")
  return number
 
#This function calculates the price after a discount and returns it. It takes 2 parameters: price and discount.
def calc_discount(price, discount):
  
  #Calculate the amount to discount and take off price
  discount_amount = price * discount
  print(discount_amount)
  price =price- discount_amount
  return price
  
#Ask the user for the price and discount amount
price = force_number("Please enter the price of the item e.g. 29.99: ")
discount = force_number("Please enter the % discount e.g. .10: ")
 
#Calculate new price and inform the user
new_price = calc_discount(price, discount)
print("The new price after", discount, "on", price, "is", new_price)

#################################################################################################
'''
Same program as above but be more explicit about how much the user saves. #FUNCTION THAT FORCES A NUMERIC INPUT
'''
# Function to force numeric input
def force_number(message):
  while True:
    try:
      number = float(input(message))
      break
    except ValueError:
      print("Please enter a number!")
  return number
 
#This function calculates the price after a discount and returns it. It takes 2 parameters: price and discount.
def calc_discount(price, discount):
  
  #Calculate the amount to discount and take off price
  discount_amount = price * discount
  print("You saved :$",discount_amount)
  price =price- discount_amount
  return price
  
#Ask the user for the price and discount amount
price = force_number("Please enter the price of the item e.g. 29.99: ")
discount = force_number("Please enter the % discount e.g. .10: ")
 
#Calculate new price and inform the user
new_price = calc_discount(price, discount)
print("The new price after", discount,"on", price,"$:",new_price)



#################################################################################################



