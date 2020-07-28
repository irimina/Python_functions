'''
Refactoring code using functions
An important part of writing code with functions is working out when and where to use them. Here are some examples:

To make our code shorter, if we have repeated chunks of code.
To future-proof our program because we know we would be likely to use that code again later on.
To make our code more readable because a descriptive function name can be easier to read in the flow of the program than the code itself.
When there is a logical breakdown of the code into functions.


A calculator can logically be broken down into functions for each mode: add, subtract, multiply, divide, powers. 
Read the comments in the editor to see how we plan to make the program.
'''

#Create a menu function that lists the modes in the calculator


#Function to get numbers from user


#Addition function


#Subtraction function


#Multiplication function


#Division Function


#Powers function


#Main program loop


##################################################################################################################

#Create a menu function that lists the modes in the calculator

def menu():
  mode = input("""Choose a mode by entering the number:
  1: Addition
  2: Subtraction
  3: Multiplication
  4: Division
  5: Powers
  6: Exit""").strip()
  return mode
#Function to get numbers from user


#Addition function


#Subtraction function


#Multiplication function


#Division Function


#Powers function


#Main program loop




##################################################################################################################

'''
Creating the add and subtract functions for the calculator.
Great, so we've broken our calculator down into some logical functions for each mode, and a menu. Let's build the functions.

'''
#Create a menu function that lists the modes in the calculator
def menu():
  mode = input("""Choose a mode by entering the number:
              "1: Addition
              "2: Subtraction
              "3: Multiplication
              "4: Division
              "5: Powers
              "6: Exit""").strip()
  return mode
  
#Addition function
def add(number1,number2):
  answer=number1+number2
  return answer

#Subtraction function
def subtract(number1,number2):
  answer=number1-number2
  return answer

#Multiplication function


#Division Function


#Powers function


#Main program loop



##################################################################################################################

'''
Create the other 3 functions for the calculator and test them
Let's build our other three functions and then under the #Main program loop comment we will test them out by passing in numbers like this:

solution = add(2, 2)
print(solution)
''''

#Create a menu function that lists the modes in the calculator
def menu():
  mode = input("""Choose a mode by entering the number:
              "1: Addition
              "2: Subtraction
              "3: Multiplication
              "4: Division
              "5: Powers
              "6: Exit""").strip()
  return mode
  
#Addition function
def add(number1, number2):
  answer = number1 + number2
  return answer

#Subtraction function
def subtract(number1, number2):
  answer = number1 - number2
  return answer

#Multiplication function
def multiply(number1,number2):
  answer=number1*number2
  return answer
  

#Division Function
def divide(number1,number2):
  answer=number1/number2
  return answer

#Powers function
def powers(number1,number2):
  answer=number1**number2
  return answer

#Main program loop. test the addition function 
solution=add(2,2)
print(solution)



##################################################################################################################

# Building the main program loop
#Main program loop


  #DRAFT Print menu and get user's mode choice
  
  
  #Check it's a valid option
  
    
    #Ask user for numbers
    
    
    #Do chosen math with numbers, or break out of loop if exit is chosen
    
    
  #Otherwise, tell the user that wasn't an option

#Farewell user when they exit


# FINAL DRAFT

#Create a menu function that lists the modes in the calculator
def menu():
  mode = input("""Choose a mode by entering the number:
              "1: Addition
              "2: Subtraction
              "3: Multiplication
              "4: Division
              "5: Powers
              "6: Exit""").strip()
  return mode
  
#Addition function
def add(number1, number2):
  answer = number1 + number2
  return answer

#Subtraction function
def subtract(number1, number2):
  answer = number1 - number2
  return answer

#Multiplication function
def multiply(number1, number2):
  answer = number1 * number2
  return answer

#Division Function
def divide(number1, number2):
  answer = number1 / number2
  return answer

#Powers function
def powers(number1, number2):
  answer = number1 ** number2
  return answer

#Main program loop
while True:
  mode=menu()
  if mode in ['1','2','3','4','5','6']:
    num1=input("Enter the first number")
    num2=input("Enter the second number")
  else:
    print("Oops, that wasn't an option, try again!")
  #Print menu and get user's mode choice
  
  
  #Check it's a valid option
  
    
    #Ask user for numbers
    
    
    #Do chosen math with numbers, or break out of loop if exit is chosen
    
    
  #Otherwise, tell the user that wasn't an option

#Farewell user when they exit

##################################################################################################################

# FINAL DRAFT

#Create a menu function that lists the modes in the calculator
def menu():
  mode = input("""Choose a mode by entering the number:
              "1: Addition
              "2: Subtraction
              "3: Multiplication
              "4: Division
              "5: Powers
              "6: Exit """).strip()
  return mode
  
#Addition function
def add(number1, number2):
  answer = number1 + number2
  return answer

#Subtraction function
def subtract(number1, number2):
  answer = number1 - number2
  return answer

#Multiplication function
def multiply(number1, number2):
  answer = number1 * number2
  return answer

#Division Function
def divide(number1, number2):
  answer = number1 / number2
  return answer

#Powers function
def powers(number1, number2):
  answer = number1 ** number2
  return answer
  
#Main program loop
while True:
  
  #Print menu and get user's mode choice
  mode = menu()
  
  #Check it's a valid option
  if mode in ["1", "2", "3", "4", "5", "6"]:
    #Ask user for numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    #Do chosen math with numbers, or break out of loop if exit is chosen
    if mode =="1":
      solution=add(num1,num2)
      print(solution)
    if mode 
    else:
      break

  else:
    print("Oops that was not an option")
      
      
      
    
  #Otherwise, tell the user that wasn't an option



##################################################################################################################
