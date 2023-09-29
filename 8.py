n = int(input("Количество чисел: "))
lst = []

for _ in range(n):
    num = int(input("Число: "))
    lst.append(num)
print(lst)
lst = lst[::2]
print("Список после удаления элементов по нечетным индексам:", lst)
