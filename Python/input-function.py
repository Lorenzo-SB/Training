name = input("Wie ist dein Name?")              #Prompt the user to enter their name
age = int(input("Wie alt bist du?"))            #Prompt the user to enter their age and convert it to an integer
height = float(input("Wie groß bist du?"))      #Prompt the user to enter their height and convert it to a float

print("Hallo " + name)                          #Print a greeting with the user's name
print("Du bist " + str(age) + " Jahre alt")     #Print the user's age
print("und " + str(height) + " cm groß.")       #Print the user's height