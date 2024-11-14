import time                         #imports the time module

for seconds in range(10,0,-1):      #creates for-clause / counts seconds in range from 10 to 0 in steps of -1
    print(seconds)                  #prints output seconds
    time.sleep(1)                   #sets the speed to 1 second
print("Frohes Neues!")              #prints output string