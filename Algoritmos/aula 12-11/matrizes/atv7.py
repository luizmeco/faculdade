import random


m1 = [[random.randint(1,10)for _ in range(4)] for _ in range(4)]
m2 = [[random.randint(1,10)for _ in range(4)] for _ in range(4)]
m3 = [[(0)for _ in range(4)] for _ in range(4)]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        m3[i][j] = max(m1[i][j], m2[i][j])

print(m1)
print(m2)
print(m3)

