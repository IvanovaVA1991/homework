# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
num = int(input('Введите число в десятичной системе '))
binum = []
def Binum(num):
    if num == 0: return []
    else:
        binum = Binum(num//2)
        binum.append(str(num % 2))
        return binum
binum = Binum(num)
binum.reverse()
print(f"Число {num} в двоичной системе - это {''.join(Binum(num))}")