# Слияние делит список на две части, сортирует и сливает их. Те две части можно сливать.
# # Сортировка слиянием

# arr1 = [3, 6, 2, 8]
# arr2 = [7, 5, 1, 9]


# arr1 = [2, 3, 6]
# arr2 = [5, 7, 8]

# [2, 3, 5, 6, 8]


# def merge_sort(list):
#     ...
#     half1 = ...
#     half2 = ...

#     half1 = merge_sort(half1)
#     half2 = merge_sort(half2)

# [
#     {
#         'name': 'John',
#         'employees': [
#             {
#                 'name': 'Henry',
#                 'employees': []
#             },
#             {}
#         ]
#     },
#     {}
# ]


# Первый вариант - разные функции (не закночил)

# arr = [1, 6, 3, 2, 7, 7, 8, 6, 8, 9]

# # Делим на два
# def separate (list):

#     new_arr_1 = []
#     new_arr_2 = []
#     i = 0
   
#     while i < len(list):
#         new_arr_1.append(list[i])
#         new_arr_2.append(list[i+1])
#         i = i+2
        
#     result  = [new_arr_1, new_arr_2]
    
#     return result


# Второй вариант  - рекурсия

arr = [1, 6, 3, 2, 7, 7, 8, 6, 9]

def separate (list_arg):

    # Делим на два
    new_arr_1 = []
    new_arr_2 = []

    i = 0
    
    for i in range(len(list_arg)):
        if i % 2 != 0:
            new_arr_1.append(list_arg[i])
        else:
            new_arr_2.append(list_arg[i])


    # Если список больше двух вызываем рекурсию
    if len(new_arr_1) > 2:
        new_arr_1 = separate(new_arr_1)
 
    if len(new_arr_2) > 2:
        new_arr_2 = separate(new_arr_2)


    # Если список меньше двух объединяем и сортируем пызырьком
    if new_arr_1 <= 2 and new_arr_2 <=2:
        z = 0
        c = []
        с = new_arr_1 + new_arr_2
        
        stop = True
        while stop:
            stop = False
            for i in range(len(c)-1):
                if c[z] > c[z+1]:
                    c[z], c[z+1] = c[z+1], c[z]
                    stop = True
        return c

    # Теперь то что вернула рекурсия сортируем слиянием
        a = 0
        b = 0
        result = []

        while True:
            if new_arr_1[a] <= new_arr_2[b]:
                result.append(new_arr_1[a])
                a = a + 1
            else:
                result.append(new_arr_2[b])
                b = b + 1

            if a >= len(new_arr_1):
                result.extend(new_arr_2[b:])
                break
            
            if b >= len(new_arr_2):
                result.extend(new_arr_1[a:])
                break

        return result
