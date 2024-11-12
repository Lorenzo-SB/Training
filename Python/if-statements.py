age = int(input("Wie alt bist du?"))
if age <= 12:    
    print("Du bist ein Säugling!")
elif age <= 16:
    print("Du bist ein Baby!")
elif age < 0:
    print("Du wurdest noch nicht geboren!")
else:
    print("Du bist Erwachsen!")

# ----------------------------------------------

temp = int(input("Wie viel Grad hat es heute?: "))

if not(temp >= 0 and temp <= 30):
    print("Heute ist das Wetter schlecht!")
    print("Bleib zu Hause!")
elif not(temp < 0 or temp > 30):
    print("Heute ist es angenehm!")
    print("Geh nach draußen!")