# ============================================
# PYTHON LESSONS - PART 1: GETTING STARTED
# ============================================

# LESSON 1: Your First Program - Hello World
# -------------------------------------------
# The print() function displays text on the screen
# Whatever you put inside the parentheses () will be shown
print("Hello World")

# This prints a friendly greeting to the screen
print("Welcome to Python!")


# LESSON 2: Printing Multiple Lines
# ----------------------------------
# You can use print() multiple times to show different messages
print("Line 1")
print("Line 2")
print("Line 3")


# LESSON 3: Variables - Storing Information
# ------------------------------------------
# A variable is like a labeled box that holds information
# Here we create a variable called 'name' and put text in it
name = "Alice"

# Now we can use that variable to display the stored information
print(name)

# Variables can hold different types of information
age = 25
print(age)


# LESSON 4: Combining Text and Variables
# ---------------------------------------
# We can combine text and variables using commas
print("My name is", name)
print("I am", age, "years old")

# Or use f-strings (put 'f' before the quotes and use {} for variables)
print(f"Hello, my name is {name} and I am {age} years old")


# LESSON 5: Basic Math Operations
# --------------------------------
# Python can do math just like a calculator

# Addition
result = 5 + 3
print("5 + 3 =", result)

# Subtraction
result = 10 - 4
print("10 - 4 =", result)

# Multiplication
result = 6 * 7
print("6 * 7 =", result)

# Division
result = 20 / 4
print("20 / 4 =", result)


# LESSON 6: Getting Input from Users
# -----------------------------------
# The input() function asks the user to type something
user_name = input("What is your name? ")

# Now we use what the user typed
print(f"Nice to meet you, {user_name}!")


# LESSON 7: Comments - Notes in Your Code
# ----------------------------------------
# Lines starting with # are comments - Python ignores them
# Comments help you (and others) understand what your code does
# This is helpful when you come back to your code later

# This prints a message
print("Comments are useful!")


# LESSON 8: Practice Exercise
# ----------------------------
# Try this: Ask for someone's favorite color and print it back
favorite_color = input("What is your favorite color? ")
print(f"Wow! {favorite_color} is a great color!")


# CONGRATULATIONS! You've completed Python Lessons Part 1!
# ---------------------------------------------------------
# You learned:
# - How to print messages
# - How to create and use variables
# - How to do basic math
# - How to get input from users
# - How to write comments