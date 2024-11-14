# print a block of symbols
rows = int(input("How many rows?: "))           #Ask the user for the number of rows and convert to an integer
columns = int(input("How many columns?: "))     #Ask the user for the number of columns and convert to an integer
symbol = input("Which symbol?: ")               #Ask the user for the symbol to use

for i in range(rows):           #Loop over the number of rows
    for j in range(columns):    #Loop over the number of columns
        print(symbol, end="")   #Print the symbol without a newline
    print()                     #Print a newline after each row

# --------------------------
# remove additional symbols (- and _)
phone_number = "1--_-23-45_67-89-1"     #Define a string with the phone number

for i in phone_number:                  #Loop through each character in the phone number
    if i == "-":                        #If the character is a hyphen
        continue                        #Skip the rest of the loop and move to the next character
    elif i == "_":                      #If the character is an underscore
        continue                        #Skip the rest of the loop and move to the next character
    print(i, end="")                    #Print the character without a newline

# --------------------------
# count from 1 to 20
for i in range(0,21):               #Loop through each character/number in range of 1 to 20 (starts with 0)

    if i == 13:                     #If the number is 13
        pass                        #Do nothing
    else:                           #For all other numbers
        print(i)                    #Print the number