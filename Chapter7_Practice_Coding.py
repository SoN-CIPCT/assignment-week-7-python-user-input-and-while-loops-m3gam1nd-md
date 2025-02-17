# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# # Chapter 7 Practice  7-1
# rentcar = input("What kind of car would yo like to rent?")
# print(f"\nLet me see if I can find you a {rentcar}")


# # Chapter 7 Practice 7-2
# party_number = input("How many people are in your dinner part?")
# party_number = int(party_number)

# if party_number < 8:
#     print(f"\nYour table is ready.")
# else:
#     print(f"\nPlease wait until a table is available.")

# # Chapter 7 Practice 7-3
# number = input("Please give me a number and I'll tell you if it is a multiple of 10.")
# number = int(number)

# if number % 10 == 0:
#     print(f"\nYour number is a multiple of 10.")
# else:
#     print(f"\nYour number is not a multiple of 10.")


# Chapter 7 Practice 7-4      
# topping = input("\nWhat toppings would you like on your pizza?")
# topping += "\n(Enter 'quit' when you are finished adding toppings.)"

# while True:
#     message = input(topping)

#     if topping == 'quit':
#         break
#     else:
#         print(f"\nI'll add {message} to your pizza.")


# Chapter 7 Practice 7-5
# age = input("\nHow old are you?")
# if age.isdigit():
#     age = int(age)

#     if age < 3:
#         print(f"\nYour movie ticket is free.") 
#     elif 3<= age <= 12:
#         print(f"\nYour movie ticket is $10.")
#     else:
#         print(f"\nYour movie ticket is $15.")
# else:
#     print("Please enter a valid number for age.")

# Exercise 7-6
#Using a conditional test and while statement
# while True:
#     age = input("\nHow old are you? ")

#     # Check if the input is a valid number
#     if age.isdigit():
#         age = int(age)

#         if age < 3:
#             print(f"\nYour movie ticket is free.") 
#         elif 3 <= age <= 12:
#             print(f"\nYour movie ticket is $10.")
#         else:
#             print(f"\nYour movie ticket is $15.")
        
#         # Exit the loop after a valid age is processed
#         break
#     else:
#         print("Please enter a valid number for age.")

# Use an active variable
# loop_active = True

# while loop_active:
#     age = input("\nHow old are you? ")

#     # Check if the input is a valid number
#     if age.isdigit():
#         age = int(age)

#         if age < 3:
#             print(f"\nYour movie ticket is free.") 
#         elif 3 <= age <= 12:
#             print(f"\nYour movie ticket is $10.")
#         else:
#             print(f"\nYour movie ticket is $15.")
        
#         # Set loop_active to False to exit the loop
#         loop_active = False
#     else:
#         print("Please enter a valid number for age.")

    # Using a break statement to exit when the user enters a quit value
# while True:
#     age = input("\nHow old are you? ")

#     if age.isdigit():
#         age = int(age)

#         if age < 3:
#             print(f"\nYour movie ticket is free.") 
#         elif 3 <= age <= 12:
#             print(f"\nYour movie ticket is $10.")
#         else:
#             print(f"\nYour movie ticket is $15.")
        
#     if age == 'quit':
#         break
#     else:
#         print("Please enter another age to check or enter 'quit when you are finished.")

# Chapter 7 Practice 7-8
# sandwich_orders = ['bacon, lettuce, & tomato', 'peanut butter and jelly', 'ham & cheese', 'meatball', 'chicken parm', 'shrimp po-boy']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"\nYour {current_sandwich.title()} sandwich has been completed.")
#     finished_sandwiches.append(current_sandwich)

# print("\nThe following sandwich orders have been made:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

# Practice 7-9
# sandwich_orders = ['bacon, lettuce, & tomato', 'pastrami', 'peanut butter and jelly', 'pastrami', 'ham & cheese', 'meatball', 'chicken parm', 'pastrami', 'shrimp po-boy']
# finished_sandwiches = []

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"\nYour {current_sandwich.title()} sandwich has been completed.")
#     finished_sandwiches.append(current_sandwich)

# print(f"\nSorry, we're all out of pastrami.")

# print("\nThe following sandwich orders have been made:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

# Practice 7-10
# responses = {}
# polling_active = True

# while polling_active:
#     name = input("\nWhat's your First Name? ")
#     dream_vaca = input("\nWhat's your dream vacation destination? ")

#     responses[name] = dream_vaca

#     repeat = input("Are there any other people who want to take the survey? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False

# print("\n--- Poll Results ---")
# for name, dream_vaca in responses.items():
#     print(f"\n{name} would like to vacation in {dream_vaca}.")