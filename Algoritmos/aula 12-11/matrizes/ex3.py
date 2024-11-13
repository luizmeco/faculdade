m1 = [ [1, 4, 2], [3, 6, 8] ]

m2 = [ [4, 1, 3], [1, 7, 3] ]

m3 = [[0] * 3 for _ in range(2)]


print(len(m1[0]))

for i in range(2):
    for j in range(3):
        m3[i][j] = m1[i][j] + m2[i][j]
    

print(m3)