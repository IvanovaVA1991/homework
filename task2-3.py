# Напишите программу, которая найдёт произведение пар чисел списка (Cписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
number = int(input('введите размер массива '))
listInt = []
for i in range(number):
    listInt.append(random.randint(0, 10))  #создали рандомный массив
print(listInt)
if number%2 != 0:
    m = number//2 + 1
else:
    m = number//2
listMult = [0]*m
for i in range(m):
    listMult[i] = listInt[i]*listInt[len(listInt)-1-i]
print(listMult)