notas = []
media = 0
count = 0

while True:
    x = float(input('Digite suas notas trimestrais (depois de adicionar tudo digite "-1":'))
    if x == -1:
        break
    else:
        media += x
        count += 1
        notas.append(x)

print(f'Suas notas foram: {notas}. A média é {media / count}.')
