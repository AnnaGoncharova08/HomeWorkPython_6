# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# a = [2, 9, 5, 9, 3]

# def summa(list):
#     sum = 0
#     for i in range(1, len(list), 2):
#         sum = sum + list[i]
#     print(sum)

# summa(a)

a = [2, 9, 5, 9, 3]
sum_odd = sum(a[item] for item in range(1, len(a), 2))
odd_el = str([a[item] for item in range(1, len(a), 2)]).strip('[]')
print(sum_odd)