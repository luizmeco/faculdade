import random

m1 = [[random.randint(1, 10) for _ in range(2)] for _ in range(2)]
m2 = [[random.randint(1, 10) for _ in range(2)] for _ in range(2)]
m3 = [[0]*2 for _ in range(2)]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        m3[i][j] = m1[i][j] * m2[i][j]

print(m1)
print(m2)
print(m3)
