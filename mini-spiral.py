# Создаем поле
def creat_field(a, b):
    field = []
    for i in range(a):
        field.append([])
        for y in range(b):
            field[i].append(0)
        print(field[i])
    return field
 
field = creat_field(7, 7) # Поле




# Ищем центр
def find_center (field_arg):
    if len(field_arg) % 2 == 0:
        y = len(field_arg) / 2 - 1
    else:
        y = (len(field) - 1) / 2
    if len(field_arg[0]) % 2 == 0:
        z = len(field_arg) / 2 - 1
    else:
        z = (len(field[0]) - 1) / 2

    return (int(y), int(z))

center = find_center(field) #Центр
print ("\n")
print (center)




# Задаем логику
def logica (hod):

    right = (0, 1)
    bottom = (1, 0)
    left = (0, -1)
    top = (-1, 0)

    if hod == right:
        proverka = bottom
        next_hod = bottom
    elif hod == bottom:
        proverka = left
        next_hod = left  
    elif hod == left:
        proverka = top
        next_hod = top
    elif hod == top:   
        proverka = right
        next_hod = right 
    
    return {"proverka": proverka, "next_hod": next_hod}




def get_proverka(hod):
    right = (0, 1)
    bottom = (1, 0)
    left = (0, -1)
    top = (-1, 0)

    if hod == right:
        return bottom
    elif hod == bottom:
        return left  
    elif hod == left:
        return top
    elif hod == top:   
        return right



# Погнали
def do_it(center_arg):

    right = (0, 1)

    y = center[0]
    z = center[1]

    field[y][z] = 1
    count = 2

    # Первый ход вправо
    hod = right
    proverka = None

    while count <= len(field) * len(field[0]):
        field[y + hod[0]][z + hod[1]] = count
        y = y + hod[0]
        z = z + hod[1]
        count = count + 1
        proverka = get_proverka(hod)

        if field[y + proverka[0]][z + proverka[1]] == 0:
            hod = logica(hod)["next_hod"]


do_it(center)


# Печатаем результат
print ("\n")   
for i in field:
    print (i)   
        

            
# ВАНИНО РЕШЕНИЕ ____________________________________________________________

def create(a):
    pole = []
    for i in range(a):
        pole.append([])
        for _ in range(a):
            pole[i].append(0)  

    return pole


# Метод ищет центр
def show (pole):
    centr = []
    for i in pole:
        
        print (f"{pole[i]} \n")
    return centr


# Метод проверяет можно ли ходить и заполняет
def turn_direction(previous_direction):
    next_direction = None
    next_check_direction = None	

    if previous_direction == (0, 1):  # Было вправо
        next_direction = (1, 0)  # стало вниз
        next_check_direction = (0, -1) # проверяем блоки слева

    elif previous_direction == (-1, 0): # Было вниз
        next_direction = (0, -1)  # стало влево
        next_check_direction = (-1, 0) # вверх

    elif previous_direction == (0, -1): # Было влево
        next_direction = (-1, 0)  # стало вверх
        next_check_direction = (0, 1) # вверх
    
    elif previous_direction == (-1, 0): # Было вверх
        next_direction = (0, 1)  # стало вправо
        next_check_direction = (1, 0) # вниз
    
    return {
        'next_direction': next_direction,
        'next_check_direction': next_check_direction
    }

    
# Цикл
def go (s, point):
    i = point['row']
    y = point['col']

    s[i][y] = 1  # Поставили 1 в центр
    s[i][y + 1] = 2 # Потсавили справа

    number = 2
    curent_direction = (0, 1)
    current_check_direction = (1, 0)
    curent_position = (i, y + 1)
    while True:
        
        # Проверяем квадрат по check direction
        element_to_check = s[
            curent_position[0] + current_check_direction[0]
        ][
            curent_position[1] + current_check_direction[1]
        ]

        if element_to_check != 0:
            number = number + 1

            curent_position = (
                curent_position[0] + curent_direction[0],
                curent_position[1] + curent_direction[1],
            )

            s[curent_position[0]][curent_position[1]] = number
        else:
            new_directions = turn_direction(curent_direction)
            curent_direction = new_directions['next_direction']
            current_check_direction = new_directions['next_check_direction']



