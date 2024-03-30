
# First I defined the first variable to ask as user_name and using input to request this information
#Then I defined the second variables to ask as user age and using input to request this information
# In order to print the requested information, I wrote a phrase between brackets to give it a grammatical sense to the requested information
#In this phrase, I used the F string format where I included both previous defined variables
# Finally, I printed the last phrase.
user_name = input("What is your name ?") 
user_age = input("Tell me your age, please")
print("Your name is {} and you are {} old".format (user_name, user_age))
print("Hello World !")