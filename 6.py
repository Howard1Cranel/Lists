import random
lst = []
for i in range(10):
    lst.append(random.randint(0, 100))
print(lst)
duplicates = set([x for x in lst if lst.count(x) > 1])
if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет")
