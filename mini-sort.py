# Классическая задача на сортировку
# Дан список чисел, числа могут повторяться, например [3, 6, 2, 15, 8, 2]
# Написать функцию, получающая отсортированный список
# В данном примере функция должна вернуть [2, 2, 3, 6, 8, 15]
# В пайтоне есть встроенная функция sorted, но не будем ей пользоваться, пока реши как захочешь, потом можно будет разобрать одни из базовых алгоритмов, алгоритмы сортировки (сортировка пузырьком, сортировка слиянием)

list = [3, 6, 2, 15, 8, 2]

# Сначала делим на уникальные и нет
def take_uni_and_double (list):
    
    result = {
    "list_uni" : [],
    "list_double" : []
    }
    for i in list:
        if i not in result["list_uni"]:
            result["list_uni"].append(i)
        else:
            result["list_double"].append(i)

    return result

new_list = take_uni_and_double(list)
new_list_uni = new_list["list_uni"]
new_list_double = new_list["list_double"]

# Потом сортируем  

def fun_sort(list_uni):

    list_uni_sort = []

    while len(list_uni) > 0:
        
        most_small = list_uni[0]
        index = 0

        for y in range (1, len(list_uni)):
            if list_uni[y] < most_small:
                most_small = list_uni[y]
                index = y

        list_uni_sort.append(most_small)
        list_uni.pop(index)            

    return list_uni_sort



new_list_uni_sort = fun_sort(new_list_uni)


# Потом добавляем повторки
def fun_add(list_double, list_uni_sort):

    for i in list_double:

        main_list = list_uni_sort
        
        # Посмотреть есть ли элемент в списке, если есть, то узнать индекс и вставить после него
        if i in list_uni_sort:
            index = list_uni_sort.index(i)
            list_uni_sort.insert(index + 1, i)
    
    return main_list # Я правильно понимаю что это только ссылка, поэтому все норм?
    

result = fun_add(new_list_double, new_list_uni_sort)

print (result)
