# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
listR = [1, 1.2, -3.1, 5.8, 10.01]
for i in range(len(listR)):
    listR[i] = abs(listR[i])
    listR[i] = listR[i]%1
print(listR)
maxElement = listR[0]
for i in range(len(listR)):
    if listR[i] > maxElement:
        maxElement = listR[i]
    else:
        i += 1
print(f'Максимальное значение дробной части: {maxElement}')
minElement = listR[0]
for i in range(len(listR)):
    if minElement != 0:
        if listR[i] != 0:
            if listR[i] < minElement:
                minElement = listR[i]
            else:
                i += 1
        else:
            i += 1
    else:
        i += 1
        minElement = listR[i]
print(f'Минимальное значение дробной части: {minElement}')
print(f'Разница между максимальным и минимальным значением дробной части элементов равна {maxElement-minElement}')