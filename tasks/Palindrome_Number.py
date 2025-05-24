# 9. Число-палиндром

# Дано целое число x, вернуть, true если x это палиндром, и false в противном случае.

# Пример 1:
# Ввод: x = 121
# Вывод: true
# Пояснение: 121 читается как 121 слева направо и справа налево.

# Пример 2:
# Ввод: x = -121
# Вывод: false
# Пояснение: Слева направо читается как -121. Справа налево становится 121-. Поэтому это не палиндром.

# Пример 3:
# Ввод: x = 10
# Вывод: false
# Пояснение: Читает 01 справа налево. Следовательно, это не палиндром.

# Ограничения:
# -2^31 <= x <= 2^31 - 1

# Продолжение: Можете ли вы решить эту задачу, не преобразуя целое число в строку?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x > 0:
            list_of_number = [int(digit) for digit in str(x)]
            if len(list_of_number) == 1:
                return True
            list_length = len(list_of_number) - 1
            point = 0
            while True:
                if list_of_number[point] == list_of_number[list_length]:
                    point += 1
                    list_length -= 1
                    if point == len(list_of_number) // 2:
                        return True
                else:
                    return False
        else:
            return True

solution = Solution()
print(solution.isPalindrome(121))
