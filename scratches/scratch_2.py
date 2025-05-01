x = 7
a = 1
fat = 1
while a <= x:
    print(f'{fat}x{a} = {fat*a}')
    fat = fat * a
    a += 1

print(fat)