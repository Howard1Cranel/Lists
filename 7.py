import random
lst = []
for i in range(10):
    lst.append(random.randint(0, 100))
print(lst)

min_index = lst.index(min(lst))
max_index = lst.index(max(lst))

print("Максимальное", max_index)
print("Минимальное",min_index)

lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
print(lst)
