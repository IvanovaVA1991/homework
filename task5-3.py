# Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
num = int(input('введите размер списка '))
list_Fibonacci = []
list_Negofib = []
def fibonacci(num):
    if num in (1, 2): return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
for i in range(1, num+1):
    list_Fibonacci.append(fibonacci(i))
def negofibonacci(num):
    if num == 1: return 0
    if num == 2: return 1
    else:
        return negofibonacci(num-2) - negofibonacci(num-1)
for i in range(1, num+2):
    list_Negofib.append(negofibonacci(i))
print(list_Negofib)
list_Negofib.reverse()
result = list_Negofib + list_Fibonacci
print(result)
