# Add a method to validate that the age input is numeric

# Function to validate age input
def get_user_age(prompt):
    while True:
        age = input(prompt)
        if age.isdigit():
            return age
        else:
            print("Please enter a valid age.")

user_name = input("What is your name? ")
user_age = get_user_age("Tell me your age, please: ")

print(f"Your name is {user_name} and you are {user_age} years old.")
print("Hello World!")