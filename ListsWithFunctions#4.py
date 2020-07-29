
# using lists with functions
# To Do List type program, where we can view our list or add items.

'''

On line 5, 
On line 8, 
On line 11 
On line 14 
On line 17 
On line 18 do the same for Freefall.
Finally, 
'''


#Create a list, Create a list called rides on line 2, and put these values in it:
# "Kamikaze", "Matterhorn", "Bumper Boats", "Freefall", "Aqualoop", "Ferris Wheel", "Gravitron"Remember to wrap the list in square brackets [].

#Append an item, use append() to add the Tea Cups ride to the end of the list.


#Insert an item, use insert() to add the Carousel to the start of the list.


#Remove an item, use remove() to delete the Matterhorn ride.


#Pop an item, use pop() to delete the Bumper Boats.


#Print out Carousel and Gravitron, using its index.

#Print a gap
print("")

#Print out the list with a loop, use a loop to print out each item in the final version of the rides list on a new line.

# final draft of this activity

#Create a list
rides=["Kamikaze", "Matterhorn", "Bumper Boats", "Freefall", "Aqualoop", "Ferris Wheel", "Gravitron"]

#Append an item
rides.append("Tea Cups")

#Insert an item
rides.insert(0, "Carousel")

#Remove an item
rides.remove("Matterhorn")


#Pop an item
rides.pop(2)

#Print out Carousel and Gravitron
print(rides[0])
print(rides[2])


#Print a gap
print("")

#Print out the list with a loop
print("These are some of the famous amusement parks ")
for ride in rides:
  print(ride)
  
  
######################################################
'''
Write the To Do List functions
Now let's break up our program into some logical functions. Here are the things we need our program to do:

Let us add tasks to our To Do list
Let us view our list
Give us instructions to choose one of those modes
Let us quit
'''

# Print out the menu so the user knows what options there are and get user's choice


# Function that allows user to add a task to their to do list


# Function that shows current tasks in the To Do List

# final draft

# Print out the menu so the user knows what options there are and get user's choice
def menu():
  mode=input("Choose an option:")
  return mode
  

# Function that allows user to add a task to their to do list
def add_tasks():
  new_task=input("Enter the task to add: ")
  todo_list.append(new_task)
  

# Function that shows current tasks in the To Do List
def view_list():
  for todo in todo_list:
    print(todo)

############################################################################################
''''
Writing the main routine for the To Do List. CREATE TSK POTENTIAL SAMPLE
Alright! 
We've got our functions made, now we just need our main program loop to run our functions. 
Oh, and to create that todo_list list that we mentioned earlier.

''''
# Print out the menu so the user knows what options there are and get user's choice
def menu():
    
  mode = input("""Choose a mode by entering the number:
  1: Add a task
  2: View list
  3: Exit
  """).strip()

  return mode

# Function that allows user to add a task to their to do list
def add_tasks():
  new_task = input("Enter the task to add: ")
  todo_list.append(new_task)

# Function that shows current tasks in the To Do List
def view_list():
  for task in todo_list:
    print("- {}".format(task))

# Create an empty list to store the tasks
todo_list=[]

# Run the main program in a loop.
repeat = True
while repeat:
  chosen_option=menu()
  if chosen_option =="1":
    add_tasks()
  elif chosen_option=="2":
    print("Here is your To Do List:")
    view_list()
  elif chosen_option=="3":
    repeat= False
  else:
    print("That was not an option")




# FInal Draft



############################################################################################
# same program
'''
Make the program more user-friendly
Cool, so our program works, but if you have a bunch of tasks to add, you have to keep pressing 1 to add them one at a time. 
It also just prints nothing if we try to view the list before we've added anything.

Let's make this program a bit more user-friendly. It will now use a loop to let the user keep adding items until they type end.

'''
# Print out the menu so the user knows what options there are and get user's choice
def menu():
    
  mode = input("""Choose a mode by entering the number:
  1: Add a task
  2: View list
  3: Exit
  """).strip()

  return mode

# Function that allows user to add a task to their to do list
def add_tasks():
  while True:
    new_task = input("Enter the task to add or type 'end' to return to menu:").strip().lower()
    if new_task == "end":
      break
    else:
      todo_list.append(new_task)
      
# Function that shows current tasks in the To Do List
def view_list():
  for task in todo_list:
    print("- {}".format(task))

# Create an empty list to store the tasks
todo_list = []

# Run the main program in a loop.
while True:
  chosen_option = menu()

  if chosen_option == "1":
    add_tasks() 
  elif chosen_option == "2":
    print("Here is your To Do List:")
    view_list()
  elif chosen_option == "3":
    break
  else:
    print("That wasn't an option, please try again")
