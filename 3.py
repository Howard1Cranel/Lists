import random
Smell = []
for i in range(10):
    Smell.append(random.randint(0, 100))
num = int(input("Введите число от 0 до 100 : "))
if num in Smell:
    print(Smell.index(num))
else:
    print("-1")
print(Smell)

