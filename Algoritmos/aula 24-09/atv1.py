notas = [7, 8, 5, 9, 7, 10]
media = 0

for nota in notas:
    media += nota

media = media/len(notas)

print(media)
print(sorted(notas))
