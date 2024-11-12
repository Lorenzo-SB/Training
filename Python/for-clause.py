# print a block of symbols
rows = int(input("Wie viele Reihen?: "))
columns = int(input("Wie viele Zeilen?: "))
symbol = input("Welches Symbol?: ")

for i in range (rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# --------------------------
# remove additional symbols (- and _)
phone_number = "1--_-23-45_67-89-1"

for i in phone_number:
    if i == "-":
        continue
    elif i == "_":
        continue
    print(i, end="")

# --------------------------
# count from 1 to 20
for i in range(0,21):

    if i == 13:
        pass
    else:
        print(i)