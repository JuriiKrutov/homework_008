def get_op():
    op = int(input('Выбирите действие:\n1. Добавить студента\n2. Добавить предмет\n3. Добавить оценку\n4. Показ списка учеников\n'
               '5. Показ листа оценок конкретного ученика\n6. Выход из программы\n'))
    return op

def input_student():
    name = input('Введите Имя и Фамилию:\n')
    return name

def input_less():
    less = input('Введите предмет:\n')
    return less

def input_mark():
    name = input('Введите имя:\n')
    less = input('Введите предмет:\n')
    mark = input('Введите оценку:\n')
    return name, less, mark

def get_name_to_show():
    name = input('Ввудите имя для просмотра оценок: \n')
    return name