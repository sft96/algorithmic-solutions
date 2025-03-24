# 1. Сумма двух

# Дан массив целых чисел nums и целое число target, вернуть индексы двух чисел, чтобы их сумма давала target.
# Вы можете предположить, что каждый вход будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.
# Вы можете возвращать ответ в любом порядке.

# Пример 1:
# Ввод: nums = [2,7,11,15], цель = 9
# Вывод: [0,1]
# Объяснение: поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].

# Пример 2:
# Ввод: числа = [3,2,4], цель = 6
# Вывод: [1,2]

# Пример 3:
# Ввод: числа = [3,3], цель = 6
# Вывод: [0,1]

# Ограничения:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Существует только один правильный ответ.

# Продолжение:  Можете ли вы придумать алгоритм, сложность которого меньше временной? O(n^2)

# O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        self.meaning = 0
        self.value = 0
        while True:
            if self.nums[self.meaning] + self.nums[self.value + 1] != self.target:
                self.value += 1
                if self.value == len(self.nums) - 1:
                    self.meaning += 1
                    self.value = 0
                    if self.meaning > self.value:
                        self.value = self.meaning
            elif self.nums[self.meaning] + self.nums[self.value + 1] == self.target:
                return [self.meaning, self.value + 1]


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
