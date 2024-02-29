teacher=input("Hello!,please let me know your name:")
print('''
    -------------------------------------------------------
    Hello ''' + teacher + ''', this is my first assignment
    -------------------------------------------------------''')

FINISH=('''
-------------------------------
this is another exercise :)
-------------------------------''')


# # #Task 1: Code Correction
# # #Below is a piece of Python code with incorrect indentation. Your task is to correct it.
# # #weather = "sunny"

# # #if weather == "sunny":
# # #print("Wear sunglasses!")
# # #else:
# # #print("Take an umbrella!")
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

# # #Task 2: Your Mood Today
# # #Ask the user how they feel today. If they say "happy", print "That's great to hear!", 
# # #and if they say "sad", print "I hope your day gets better!". 
# # #Ensure your if statement is properly indented
print(FINISH)

user_feelings = input("How do you feel today "+ teacher+"? (Happy)-(Sad) ")

while user_feelings != "happy" or user_feelings != "sad":
    if user_feelings == "happy" or user_feelings == "sad":
        break
    else:
        user_feelings = input("Sorry, I didn't hear you, can you tell me how do you feel today? ")
if user_feelings == "happy":
    print("That's great to hear!")
elif user_feelings == "sad":
    print("I hope your day gets better!")

print(FINISH)
    
# # #Task 3: Spotting Indentation Errors
# # #Read the following code. Is the indentation correct?
# # #mood = "excited"
# # #if mood == "excited":
# # #    print("Yay! Let's have fun.")
# # #    else:
# # #print("Let's find something fun to do!")
# # #If the indentation is wrong, correct it.
mood = "excited"
if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!")

print(FINISH)
# # # Task 1: Create a Poem using Comments
# # # Craft a short poem about Python. 
# # # Each line of the poem should be a single-line comment.

#In forests deep, where shadows weave,
#Python slithers, silent eve.
#Its scales a dance, a rhythmic glide,
#In nature's code, it doth confide.

# # #Task 2: Multi-line Poem
# # #Now, craft a multi-line poem about Python. 
# # #Instead of using single-line comments, 
# # #use triple quotes to make it a multi-line comment. Here's an example:
'''
In the jungle of code, where whispers flow,
Python reigns, silent yet aglow.
With power unmatched, its prowess clear,
In lines of code, its dominance peers.
In syntax wild, its elegance gleams,
'''

# # # Task 3: Combining Single and Multi-line Comments
# # #Choose one line from your single-line comment poem and another line from your multi-line comment poem. Put these lines into a new Python script and separate them with a descriptive single-line comment about each.

# # #For instance:

# This line is from my first poem
#In nature's code, it doth confide.

# This line is from my multi-line poem
'''
In syntax wild, its elegance gleams,
'''
# # #Task 1: Code Correction
# # #You have been given a piece of code with several variable and constant names that don't follow the Python naming convention. 
# # #Your task is to correct them:
# # #Pi_value = 3.14
# # #userAge = 25
# # #user_location = "New York"
# # #MAXLIMIT = 1000
PI_VALUE = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

# # #Python Data Types and type() Function
# # #Objective:
# # #The aim of this assignment is to practice identifying and using Python's basic data types, as well as the type() function for checking a variable's data type.

# # #Task 1: Code Correction
# # #Given below are some variable assignments. Your task is to identify the data type of each variable and then use the type() function to print it out:

variable_a = "Hello, World!"
variable_b = 23
variable_c = 3.14
variable_d = True
print(type(variable_a))
print(type(variable_b))
print(type(variable_c))
print(type(variable_d))

# # # Task 1: Code Correction
# # # Below is a piece of code where a variable's data type changes. 
# # # Your task is to print the type of the variable after each assignment to see the dynamic nature in action:
print(FINISH)
dynamic_variable = "This is a string"
print(type(dynamic_variable))

dynamic_variable = 100
print(type(dynamic_variable))

dynamic_variable = 25.5
print(type(dynamic_variable))

print(FINISH)

# # # 6.) Arithmetic Operations in Daily Life
# # # Objective:
# # # The aim of this assignment is to get familiarized with basic arithmetic operations and understand how they can be applied in everyday situations.

# # # Tasks:

# # # Task 1: Grocery Store Math
# # # Calculate the total cost of three items you'd commonly find in a grocery store,
# # # given their individual prices.
milk=1
suggar=3
bread=5
print ("bread cost $" + str(bread))
print("suggar cost $"+ str(suggar))
print("milk cost $"+ str(milk))
total_cost=(milk+suggar+bread)
print("total is $" + str(total_cost))

print(FINISH)
# # # Task 2: Bank Interest
# # # If you have a savings account with a particular initial amount and a fixed yearly interest rate, 
# # # calculate the total amount in your account after a year.
bank_account=3000000
interest_per_year= bank_account/100*3
bank_account=bank_account + interest_per_year
print("$"+str(bank_account))
print(FINISH)
# # # Task 3: Area and Perimeter
# # # Given the length and width of a rectangle, compute both its area and perimeter using arithmetic operators.
length=5
width=6
area=length*width
perimeter=length*2+width*2
print("the area of the rectangle is "+ str(area))
print("the perimeter of the rectangle is "+ str(perimeter))

print(FINISH)

# # # 7.) Understanding Assignments and Comparisons
# # # Objective:
# # # The aim of this assignment is to get a grasp on how assignment 
# # # operators work and how values can be compared using comparison operators.

# # # Tasks:

# # # Task 1: Value Swapping
# # # Swap the values of two given numbers using assignment operators and then compare them to ensure they have been swapped.
value1=5
value2=10
value1,value2=value2,value1
if value2<value1:
    print("values swaped!")
        
print(FINISH)
# # # Task 2: Perfect Square Checker
# # # Given a number, determine if it's a perfect square (like 1, 4, 9, 16, …). Hint: You might need the exponentiation operator for this.
number=5
if number**0.5%1==0:
    print("a perfect square")
else: print("not a perfect square")

print(FINISH)

# # # 8.) Exploring Logical Operations and Precedence
# # # Objective: The aim of this assignment is to grasp the concept of logical operations and understand how operator precedence can affect the outcome of an operation.

# # # Tasks:

# # # Task 1: Simple Logic Puzzles Given a set of True or False values, use the AND, OR, and NOT operators to come up with a desired True or False outcome.
is_sunny=True
is_rainning=False
too_sunny=True
use_solarprotection=True
cloudy=False
if too_sunny and cloudy==False:
    use_solarprotection=True
    print("use solar protection!")
if not too_sunny:
    use_solarprotection=False
    print("dont use solar protection")
if is_rainning or cloudy:
    use_solarprotection=False
    print("dont use solar protection")

print(FINISH)

# # # Task 2: Validating Calculations Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.
result1=5+5*5
result2=(5+5)*5
if result1!=result2:
    print("the results do not match")
    print('''first operation is '''+str(result1))
    print('''second operation is ''' +str(result2))
    
print(FINISH)    
# # # Task 3: Mix and Match Combine arithmetic, logical,
# and comparison operators in a single expression and predict the outcome.
# Then, compute the expression to see if the prediction was correct.
#i think the result is going to be number3=3+5 that is 8 so result is going to be 4+5*8
number1=4
number2=5
number3=3
if number1<=number2 or number2*number3 > 5:
    result = number1+number2+number3

print(result)

print('''
     ---------------------------------------------------------------------
      This is the end of the assignment i hope you are having a great day!
     ---------------------------------------------------------------------''')