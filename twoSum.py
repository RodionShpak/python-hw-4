# from typing import List
# Дано масив цілих чисел nums і ціле число, 
# поверніть індекси двох чисел так, щоб їх сума дала передане ціле число.
# Ви можете припустити, що кожен вхід матиме рівно одне рішення, 
# і ви не можете використовувати той самий елемент двічі.
# Ви можете повернути відповідь у будь-якому порядку.
# def twoSum(nums: List[int], target: int) -> List[int]:
#     print(nums, target)

# twoSum([1, 2, 3], 4)        # [0, 2]
# twoSum([2, 7, 11, 15], 9)   # [0, 1]
# twoSum([3, 2, 4], 6)        # [1, 2]
# twoSum([3, 3], 6)           # [0, 1]
# # 
# 
# 
# 
# 
# Задача має багато варіантів реалізації


# 1 варіант
# Суть полягає в створені словника, 
# де зберігатимемо числа в масиві, як ключів, для перевірки повторного зустрічання. 
# Під час проходження ми записуємо як індекс, так і значення. Під час обходу кожного числа ми обчислюємо інше число, 
# яке нам потрібно, щоб отримати суму. Це друге число, яке нам потрібне, є різницею - ціль - target, 
# яку ми шукаємо в наших ключах словника
# nums = [2, 7, 11, 15]
nums = [3, 2, 4]
target = int(6)
# target = int(9)
def twoSum(nums, target):                     
        seen_values = {}
        for index, value in enumerate(nums):                     # Через функцію enumerate - для циклічного перебору з автоматичною індексацією, що згенерована змінною лічильником, замість range(len (...))
            if target - value in seen_values:
                return seen_values[target - value], index
            else:
                seen_values[value] = index
        return -1
print(list(twoSum(nums, target)))


# 2 Варіант
# lisT = [2, 7, 11, 15]
# number = int(9)
# def two_sum(lisT, number):
#         storedNums = {lisT[0]: 0}
#         for i in range(1, len(lisT)):
#             number = number - lisT[i]
#             if number in storedNums.keys():
#                 return [storedNums.get(number), i]  # за допомогою методу get(), який повертає значення для заданого ключа. Якщо ключ недоступний, повертає значення за замовчуванням None
#             storedNums[lisT[i]] = i
#         return [-1,-1]
#         list(two_sum)
# print(two_sum(lisT, number))

# 3 Варіант

# nums = [1, 2, 3] 
# target = int(4)
# def twoSum(nums, target):
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if (nums[i] + nums[j]) == target:
#                     return [i,j]
#         return [-1,-1]
# print(twoSum(nums, target))

# 4 Варіант 


# nums = [2, 7, 11, 15]
# target = int(9)
# def twoSum(nums, target):
#     dict = {}                         # Створюємо словник, який буде містити кожен елемент списка в ролі ключа
#     for i in range(len(nums)):             # Перебираємо число в списку і додаємо його в словник
#         dict[nums[i]] = i
#     for i in range(len(nums)):        # Знову перебираэмо список, щоб знайти число, яке задовільняє рівнянню 
#         x = target - nums[i]
#         if x in dict and dict[x] != i:   # Перевіряємо чи находиться число Х в словнику
#             return [i, dict[x]]
#     return []
# print(twoSum(nums, target))