# for loop - runs a finite amount of times
# fav_drinks=[
#     "juice",
#     "tea",
#     "Water"
# ]

# for i in fav_drinks:
#     print("A great choice!") # 'i' is the iteration variable. 'i' changes to the next element in the sequence. 'i' can be called anything.
# -------------------------------------------------
# for i in range(2,12,2):
#     print(i)
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)
# -----------------------------------------------
#While loop
# answer = input("Who ordered a cortado?")

# if answer !="Alex":
#     print("incorrect")
#     answer = input("Who ordered a cortado?")
# else: 
#     print("correct")
# ------------------------------------------------
#Activity 1 - create a for loop that prints "Hello World!" 13 times
# for i in range(1,14):
#     print("Hello World!")
#While loop
# count = 0
# while count < 14:
#     print("Hello World!")
#     count += 1
# ------------------------------------------------
#Activity 2 - Nested for loop, multiplication table from 1 to 12
# for i in range(1,13):                          # Outer loop for numbers 1 to 12 
#     print(f"Multiplication Table for {i}:")
#     for j in range(1,13):                      # Inner loop for multiplying by 1 to 12
#         print(f"{i} x {j} = {i * j}")             
#     print("------")                              # print a  line after each table
# ------------------------------------------------
#Activity 3 - log-in program that asks a user to enter a password to continue. The user cannot continue until they get the password correct.
#Set correct password
# correct_password = "BabyCakes"

# # Set maximum amount of attempts
# max_attempts = 3
# # Attempt counter
# attempts = 0

# # Loop to allow user to try up to max_attempts times
# while attempts < max_attempts:
#     password = input("Enter your password to continue: ")
#     if password == correct_password:
#         print("Access granted!")
#         break
#     else:
#         attempts += 1
#         print(f"Incorrect password. You have {max_attempts-attempts} attempts left. Please try again.")
#     if attempts == max_attempts:
#         print("Too many failed attempts. You are locked out.")
# --------------------------------------------------