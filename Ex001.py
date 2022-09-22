# 3 Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# l = [1, 1, 1, 5, 55, 7, 3, 99, 9, 9]
# new_l = []
# count = 0
# for i in l:
#     if i not in new_l:
#         new_l.append(i)
# print(new_l)

l = [1, 2, 3, 4, 4, 3, 8, 9, 1]
result_list = list(filter(lambda a: l.count(a) == 1, l))
print(result_list)