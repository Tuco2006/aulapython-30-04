num = int(input('Digite um número:'))
i = 1
primo = True
while i <= num:
    if num % i != 0:
        primo = False
    i = i + 1

if primo or num == 1:
    print(f'{num} é primo!')
else:
    print(f'{num} não é primo!')
