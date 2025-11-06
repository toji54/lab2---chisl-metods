system = [
    [2, 1, 1, 1, 2],
    [2, 2, 1, 1, 3],
    [2, 2, 2, 1, 3],
    [2, 2, 2, 3, 1]
]

"""### Прямой ход"""

def search_mult(i_main):
    # j_main - индекс столбца, в котором находится main элемент
    j_main = i_main
    main_value = system[i_main][j_main]

    # Находим ненулевой ведущий элемент
    if main_value == 0:
        for i in range(i_main + 1, len(system)):
            if system[i][j_main] != 0:
                # Меняем строки местами
                system[i_main], system[i] = system[i], system[i_main]
                main_value = system[i_main][j_main]
                break

        # Если все элементы в столбце j_main нулевые, пропускаем этот шаг
        if main_value == 0:
            return []

    lst_mult = []

    for i in range(i_main + 1, len(system)):
        if system[i][j_main] == 0:
            continue

        mult = -system[i][j_main] / main_value
        lst_mult.append((i, mult))

    return lst_mult


for i_main in range(len(system) - 1):
    lst_mult = search_mult(i_main)

    for i_value, mult_value in lst_mult:
        # Обновляем только ОДНУ строку - i_value
        for j in range(len(system[i_value])):
            system[i_value][j] += system[i_main][j] * mult_value

print("Треугольная матрица после прямого хода:")
for row in system:
    print([f"{x:.2f}" for x in row])

"""### Обратный ход"""

result = {i+1: None for i in range(len(system))}

for i in range(len(system)-1, -1, -1):
    summ = 0
    for j in range(i+1, len(system)):
        summ += system[i][j] * result[j+1]

    result[i+1] = (system[i][len(system[i])-1] - summ) / system[i][i]

print("Решение системы:")
for key in result:
    print(f'x{key} = {result[key]}')