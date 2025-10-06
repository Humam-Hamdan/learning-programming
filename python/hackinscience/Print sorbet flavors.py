FLAVORS = ["Banana", "Chocolate", "Lemon", "Pistachio", "Raspberry", "Strawberry", "Vanilla"]
x = 0
y = 0
for j in range(7):
    print(FLAVORS[x]); x += 1
    for i in range(7):
        print(FLAVORS[y])
        y += 1
        if y == 7:
            pass