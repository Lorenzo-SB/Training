rows = int(input("Wie viele Reihen?: "))
columns = int(input("Wie viele Zeilen?: "))
symbol = input("Welches Symbol?: ")

for i in range (rows):
    for j in range(columns):
        print(symbol, end="")
    print()