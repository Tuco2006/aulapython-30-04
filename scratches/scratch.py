num = int(input('Digite um número:'))
div = (num % num)
div2 = (num % 1)

while num != 0:
    num3 = num - 1
    div3 = num % num3
    if div3 != 0 and div == 0 and div2 == 0:
            print('Esse número é primo!')
    else:
            print('Esse número não é primo!')
    num = num3





