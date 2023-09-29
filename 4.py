import random
Damn = []
summa = 0
multi = 1
for i in range(1, 11):
    Damn.append(random.randint(0, 100))
for y in Damn:
    summa += y
    multi *= y
print(Damn)
print(f"Сумма {summa}. Произведение {multi}")
    
