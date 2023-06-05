import random



def find_max_even_index(arr):
    max_value = float('-inf')
    for i in range(0, len(arr), 2):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value

my_array = [3, 8, 2, 10, 5, 6, 7]
max_even = find_max_even_index(my_array)

print("Задание 1")
print("Максимальный элемент с четным индексом:", max_even)
print("\n")



def find_elements_less_than_average(arr):
    average = sum(arr) / len(arr)
    result = []
    for element in arr:
        if element < average:
            result.append(element)
    return result


my_array = [3, 8, 2, 10, 5, 6, 7]
elements_less_than_average = find_elements_less_than_average(my_array)
print("Задание 2")
print("Элементы, значения которых меньше среднего арифметического:", elements_less_than_average)
print("\n")



def find_two_smallest_elements(arr):
    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if num <= smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num

    return smallest, second_smallest


my_array = [5, 2, 8, 3, 3, 10, 7]
smallest, second_smallest = find_two_smallest_elements(my_array)
print("Задание 3")
print("Первый наименьший элемент:", smallest)
print("Второй наименьший элемент:", second_smallest)
print("\n")


def sum_of_digits(arr):
    total_sum = 0
    for num in arr:
        digits = str(num)
        for digit in digits:
            total_sum += int(digit)
    return total_sum

# Пример использования
my_array = [123, 45, 678, 9]
digits_sum = sum_of_digits(my_array)
print("Задание 4")
print("Сумма всех цифр в массиве:", digits_sum)
print("\n")


def average_of_positive_elements(arr):
    positive_elements = [num for num in arr if num > 0]
    if not positive_elements:
        return 0
    return sum(positive_elements) / len(positive_elements)


my_array = [-2, 3, 5, -1, 8, -4, 6]
average = average_of_positive_elements(my_array)
print("Задание 5")
print("Среднее арифметическое положительных элементов:", average)
print("\n")



def swap_min_max(arr):
    if len(arr) < 2:
        return arr

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

    return arr


my_array = [5, 2, 8, 3, 2, 10, 7]
swapped_array = swap_min_max(my_array)
print("Задание 6")
print("Массив с поменяными местами минимальным и максимальным элементами:", swapped_array)
print("\n")



def calculate_matrix_stats(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    total_sum = 0
    total_product = 1

    for i in range(rows):
        for j in range(cols):
            total_sum += matrix[i][j]
            total_product *= matrix[i][j]

    average = total_sum / (rows * cols)

    return total_sum, total_product, average


my_matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

sum_matrix, product_matrix, average_matrix = calculate_matrix_stats(my_matrix)
print("Задание 7")
print("Сумма элементов матрицы:", sum_matrix)
print("Произведение элементов матрицы:", product_matrix)
print("Среднее арифметическое элементов матрицы:", average_matrix)
print("\n")



def calculate_diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        return 0

    diagonal_sum = 0

    for i in range(rows):
        diagonal_sum += matrix[i][i]

    return diagonal_sum


my_matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

sum_diagonal = calculate_diagonal_sum(my_matrix)
print("Задание 8")
print("Сумма элементов главной диагонали матрицы:", sum_diagonal)
