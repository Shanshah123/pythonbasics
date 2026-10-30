# Build a menu-driven program that runs until the user selects “Exit”.
# print('Welcome to My Calculator')

# Num1 = int(input('enter number 1:'))
# Num2 = int(input('enter number 2:'))


# while True:
 
#  print(1,'Add')
#  print(2,'Sub')
#  print(3,'Multiply')
#  print(4,'Division')
#  print(5,'Exit')

#  Option = int(input('What is your operation you want me to do:'))

#  if Option == 1:
    
#   print(Num1 + Num2)
    
#  elif Option == 2:
    
#   print(Num1 - Num2)

#  elif Option == 3:
    
#   print(Num1 * Num2)

#  elif Option == 4:
  
#   print(Num1/Num2)
    
#  elif Option ==5:
  
#   print('Thank you for using the program')
#   break

 
# Keep reading user input until the input is a valid integer.

# Integer = input('enter the input:')

# while not Integer.isdigit():
#     print('Invalid output')
#     Integer = input('enter the input:')

# print('Valid integer',Integer)

 
# Simulate a retry system:

# Allow max 3 attempts

# Stop early if successful

# for login in range(3):
#   Username = (input('enter username:'))
#   Password = int(input('enter password:'))

#   if Username =='Sharukh123' and Password == 144445:
#     print('login Successfully')
#     break
#   elif Username != 'Sharukh123' and Password != 144445:
#     print('Invalid Username and Password')
#   elif Username != 'Sharukh123':
#     print('Invalid Username')
#   elif Username != 144445:
#     print('Invalid Password')
# else:
#   print('Maximum attempt reached')

      


# Use a loop to simulate a countdown timer.
# Timer = int(input('enter timer:'))

# for i in range(Timer,0,-1):
#     print(i)
# print('Stop')
    
    
  

# Process a log file (list of strings) and count how many times each error code appears.

# logs = [
#     "ERROR 404",
#     "ERROR 500",
#     "ERROR 404",
#     "ERROR 403",
#     "ERROR 500", 
#     "ERROR 404"
# ]

# count = {}

# for error in logs:
#     code = error.split()[1]
#     if code in count:
#       count[code]+=1
#     else:
#       count[code]= 1
# print(count)


# Use loops to find the longest streak of consecutive numbers in a list.

# Numbers = (
# 4,5,5,6,7,8,9,10,1,1,2
# )


# longest =1
# count = 1

# for i in range(1,len(Numbers)):
#     if Numbers[i] == Numbers[i-1]+1:
#         count+=1
#     else:
#         count ==1
#     if count>longest:
#         longest = count
 
# print('Longest Streak',longest)

# Simulate a basic recommendation system:

# Loop through user preferences
# Match them against available items
# print('Amazon Shopping App')

# cart = [
#     "Laptop",
#     "Mobile Phone",
#     "Headphones",
#     "Keyboard",
#     "Mouse",
#     "T-Shirt",
#     "Shoes",
#     "Watch",
#     "Backpack",
#     "Water Bottle"
# ]

# while True:
#     preference = input('Enter needed item to shop: ')

#     for carts in cart:
#         if carts.lower() == preference.lower():
#             print('Item Available, Added to Cart')
#             break
#     else:
#         print('Not Available')
#         break


# Given a list of dictionaries (users), use loops to find:

# Active users
# Users older than 30
# Users with missing fields


# Users = [
#     {"name": "Rahul", "age": 25, "city": "Mumbai", "active": True},
#     {"name": "Priya", "age": 30, "city": "", "active": False},
#     {"name": "Arun", "age": 22, "city": "Chennai", "active": True},
#     {"name": "Sneha", "age": 28, "city": "Kerala", "active": True},
#     {"name": "Vijay", "age": 35, "city": "Hyderabad", "active": False}
# ]
# for User in Users:
#     if User["active"] == True:
#         print('Active Users are',User["name"])
        
#     elif User["age"] > 30:
#         print('People older than 30',User["name"],User["age"])
#     elif User["name"]=="":
#         print('Missing Field',User["name"])
#     elif User["age"]=="":
#         print('Missing Field',User["name"])
#     elif User["city"]=="":
#         print('Missing Field',User["name"])
    

# Rewrite a traditional loop using:

# enumerate()
# zip()

# Students = ['Sharukh','Jake','Scully','Amy']
# Marks = [50,80,90,100]

# for i,(student,mark) in enumerate(zip(Students,Marks)):
#     print(i,student,mark)


# Identify and fix an inefficient loop that causes unnecessary repeated work.

cart = [
    "Laptop",
    "Mobile Phone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "T-Shirt",
    "Shoes",
    "Watch",
    "Backpack",
    "Water Bottle"
]

while True:
    preference = input('Enter Item')
    found = False
    for carts in cart:
     if carts.lower() == preference.lower():
        print('Item Available added to cart')
        found = True
        break
    else:
        print('Item Not Available in Cart')
        break
