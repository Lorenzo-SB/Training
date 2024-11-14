age = int(input("Wie alt bist du?"))        #Prompt the user to input their age and convert it to an integer

if age <= 12:                               #Check if the age is 12 or less
    print("Du bist ein Säugling!")          #If true print that the user is an infant

elif age <= 16:                             #Check if the age is 16 or less (but greater than 12)
    print("Du bist ein Baby!")              #If true print that the user is a baby

elif age < 0:                               #Check if the age is less than 0
    print("Du wurdest noch nicht geboren!") #If true print that the user is not born yet

else:                                       #If none of the above conditions are true the user is considered an adult
    print("Du bist Erwachsen!")             #Print that the user is an adult
# ----------------------------------------------------------------------------
temp = int(input("Wie viel Grad hat es heute?: "))  #Prompt the user to input the temperature and convert it to an integer

if not(temp >= 0 and temp <= 30):                   #Check if the temperature is not between 0 and 30 degrees inclusive
    print("Heute ist das Wetter schlecht!")         #If true print that the weather is bad
    print("Bleib zu Hause!")                        #Suggest staying at home

elif not(temp < 0 or temp > 30):                    #Check if the temperature is between 0 and 30 degrees inclusive
    print("Heute ist es angenehm!")                 #If true print that the weather is pleasant
    print("Geh nach draußen!")                      #Suggest going outside