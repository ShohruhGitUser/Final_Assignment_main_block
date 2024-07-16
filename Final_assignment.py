def find_short_strings(arr):
    result = []
 
    for string in arr:                 # Проверяем длину строки
        if len(string) <= 3:        # Если строка удовлетворяет условию,    добавляем ее в результирующий массив
            result.append(string)
    return result



# Ввод  строк с клавиатуры пользователем
input_string = input("Введите строки через пробел: ")
input_array = input_string.split()                                          # Разделяем введенную строку на отдельные элементы

output_array = find_short_strings(input_array)
print(output_array)  # Вывод результата