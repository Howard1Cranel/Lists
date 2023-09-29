Fear = [0]

for i in range(101):
        if i == 1:
                Fear.append(1)
                Fear.reverse()
        if i == 100:
                Fear.append(1)
        else:
                Fear.insert(i,0)
print(Fear)
