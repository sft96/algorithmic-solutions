# Бинарный поиск

# Дан массив целочисленных отсортированных значений array и целевое значение target
# array = [1, 3, 5, 8, 9, 12, 16]
# target = 12

# Найти индекс target в массиве array за O(logn)

# O(logn)
def BSearch(array, target):
    left = 0
    right = len(array)
    while right > left:
        middle = (left + (right - 1)) // 2
        if target == array[middle]:
            return middle
        elif target > array[middle]:
            left = middle + 1
        elif target < array[middle]:
            right = middle
    return None


print(BSearch([1, 3, 5, 8, 9, 12, 16], 12))
