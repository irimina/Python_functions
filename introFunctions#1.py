'''
A function is a named, reusable chunk of code that can be called from anywhere in a program. 
It makes your code modular so bits can be run out of order, or multiple times, without having to rewrite all of the code each time.

Let's get into it! This lesson gives you a preview of the kinds of things you'll learn, so don't worry if there are parts that are a bit confusing right now, 
it will all be explained soon.
In the code editor is a function called hello_world().

'''


#Create a function that prints "Hello, world!"
def hello_world():
  print("Hello, world!")
  
#Run the hello_world function

#########################################################################
'''
You already know heaps about functions from the built-in Python ones!
Functions have a name, and to use them you write that name and brackets e.g.int().
Sometimes you put information (arguments) in the brackets e.g. print("Hello!") or my_list.insert(0, "bobcat")
'''

#Create functions that will add to a number passed in.
def add_10(number):
  print(number + 10)
  
def add_20(number):
  return number + 20

#Call the add_10 function
add_10(5)

#Call the add_20 function
print(add_20(5))

#########################################################################
'''
The anatomy of a function
Let's take a closer look at how a function is structured:

def my_function(a_parameter, or_more):
   #Code that does stuff
   return a_value, maybe_more
To define a function we use the def keyword. The function is given a name, and in Python we use lower_with_under, just like variable names.

Inside the brackets we can set some parameters if we need to be able to pass in values, or we can leave them empty.
In the block inside the function, we put the code that does stuff, and then we might return one or more values using return.
'''

#A function that multiplies a number by 2 and returns it. Replace the ???
??? times_by_2(number):
  result = number ???
  ??? result



#A function that multiplies a number by 2 and returns it
def times_by_2(number):
  result = number * 2
  return result

print(times_by_2(7))
#########################################################################
#When to use a function. - Try/Except on comparing numbers
'''
Functions should be used when you have a job or process that needs to happen in your code more than once. Each function should have 1 purpose, 
rather than just filling it with a bunch of different tasks.

Take a look at the code in the editor. We are using try/except to force the user to enter 2 valid numbers and telling them which is higher.

This is a great example of when a function is useful, because we have to write the try/except block out twice.
'''

#Ask the user for a number
while True:
  try:
    num_1 = int(input("Please enter a number: "))
    break
  except ValueError:
    print("That was not a valid number!")
    
#Ask the user for a second number
while True:
  try:
    num_2 = int(input("Please enter another number: "))
    break
  except ValueError:
    print("That was not a valid number!")

if num_1 > num_2:
  print("Your first number", num_1, "was higher than your second number", num_2)
elif num_2 < num_1:
  print("Your first number:", num_1," was lower than your second number", num_2)
else:
  print("The numbers are equal")
#########################################################################
# Refactor higher/lower code using a function
# So, since we need to force a valid number twice in our program, it makes sense to turn that code into a function.
'''
We have defined a function called force_number(). 
It has one parameter called message which means we can pass in the message we want to use when we ask for input e.g. 
Please enter a number:  or How old are you? This makes the function more flexible than just hard-coding the message.
'''
#Create a function to force a valid number
def force_number(message):
  while True:
    try:
      number = int(input(message))
      break
    except ValueError:
      print("That was not a valid number!")  
  return number
    
#Ask the user for 2 numbers
num_1 = force_number("Please enter a number:")
num_2 = force_number("Please enter another number:")

if num_1 > num_2:
  print("Your first number {}, was higher than your second number {}".format(num_1, num_2))
else:
  print("Your second number {}, was higher than your first number {}".format(num_2, num_1))
  
#########################################################################
# create a function with user input
'''
Let's make a new function from scratch this time, and make it a bit more interactive.

Functions use blocks like loops, and if statements, so code that is included in the function is the code that is indented:

def my_function():
  print("I'm inside the function!")
  print("I'm also inside the function!")

print("I'm outside the function!")
'''
#Create a function that says hello to the user
def hello_user():
  name=input("What is your name?")
  print("Hello", name)
hello_user()


#########################################################################


#Create a perimeter function for a rectangle
def calc_perimeter():
  length = float(input("What is the length of the rectangle in cm? "))
  width = float(input("What is the width of the rectangle in cm? "))
  perimeter = 2 *length + 2 * width
  print("The perimeter is ",perimeter)
 
calc_perimeter()



#########################################################################

# local vs global variables
# print the length and the width variables outside their functions - ERROR


#Create a function that does an area calculation
def calc_area():
  length = float(input("What is the length of the rectangle in cm? "))
  width = float(input("What is the width of the rectangle in cm? "))
  area = length * width
  print("The area is: {}cm".format(area))
 
calc_area()



#Create a perimeter function for a rectangle
def calc_perimeter():
  length = float(input("What is the length of the rectangle in cm? "))
  width = float(input("What is the width of the rectangle in cm? "))
  perimeter = 2 * length + 2 * width
  print("The perimeter is: {}cm".format(perimeter))

calc_perimeter()


#########################################################################
'''
Setting parameters for a function
Now that we have put the code for the area and perimeter functions together in one program, there is some repeated code. 
It would be useful if we only had to ask for the measurements once, and then we could tell the user both calculations using the same measurements. 
That's what parameters are for!
'''


