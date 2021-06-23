# Task 1

num = 0
# For loop that repeats hello 10 times
for num in range(10):
    print("hello")
    num += 1

# Task 2
# Creating empty lists
list_names = []
list_names_lower = []

# While loop asking for name input or other options
while True:
    name = input("Add a name to the list:"
                 "\nType 'list' to see the list:"
                 "\nType 'lower_list' to see the lower case names list"
                 "\nor type 'exit' to quit the program:    ")
    if name == "lower_list":  # If user asks for lower case list, the lower case list is shown
        print(list_names_lower)
    if name == "list":  # If user asks for normal case list, the normal list is shown
        print(list_names)
    if name == "exit":  # If user asks to exit, the program breaks out the loop
        break
    else:
        list_names.append(name)  # If anything else is entered, the data is added to the list
        list_names_lower.append(name.lower())  # The name is also converted into lower case and stored on the lower case list
        if len(name) % 2 == 0:  # If the string has no remainder when divided by 2 (even) it tells the user
            print(f"The name: {name} has an even number of letters")
        else:  # If the string has a remainder when divided by 2 (odd) it tells the user
            print(f"The name: {name} has an odd number of letters")
