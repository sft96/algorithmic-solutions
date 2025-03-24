# Бинарный поиск

# Дан массив целочисленных отсортированных значений array и целевое значение target
# array = [1, 3, 5, 8, 9, 12, 16]
# target = 12

# Найти индекс target в массиве array за O(log n)

# O(log n)
array = [1, 3, 5, 8, 9, 12, 16]
target = 12
description = f"The number {target} is missing from the array"
def BSearch(array, target):
    left_index = 0
    right_index = len(array)
    while right_index > left_index:
        middle = (left_index + (right_index - 1)) // 2
        if target == array[middle]:
            return middle
        elif target > array[middle]:
            left_index = middle + 1
        elif target < array[middle]:
            right_index = middle
    return description


print(BSearch(array, target))
