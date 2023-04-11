current_users = ['admin123', 'johndoe', 'janedoe', 'superuser', 'foobar']
new_users = ['johndoe', 'janedoe', 'newuser', 'anotheruser', 'foobar']

# Create a lowercase copy of the current_users list
current_users_lower = [user.lower() for user in current_users]

# Loop through each new user and check if their username has already been used
#for user in new_users:
    ####print(f"The username '{user}' is available.")
numbers= [1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num == 1: 
        print(f"'{num}'st")
    elif num==2:
        print(f"'{num}'nd")
    elif num==3: 
        print(print(f"'{num}'rd"))
    else:
        print(print(f"'{num}'th"))
