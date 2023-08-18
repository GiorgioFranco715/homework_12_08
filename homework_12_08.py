#Завдання 4(а):
#Розв'язок задачі:
# def menu():
#      if user_choise == "Відображення списку":
#          return print(new_list)
#      elif user_choise == "Отримання максимального значення у списку":
#          return print(max(new_list))
#      elif user_choise == "Отримання мінімального значення у списку":
#          return print(min(new_list))
#      if user_choise == "Відображення значення елемента за індексом, введеним користувачем":
#          index_from_list = int(input("Введіть індекс зі списку який вас цікавить:"))
#          return new_list[index_from_list - 1]
#
#      elif user_choise == "Видалення елемента за індексом, введеним користувачем":
#          index_for_delete = int(input("Введіть індекс зі списку який вас цікавить:"))
#          if index_for_delete > quantity_elements :
#              return ("користувач ввів неправильне значення для індексу елемента в списку")
#          else:
#              del new_list[index_for_delete - 1]
#              return print(new_list)


# Завдання 4(b):
# Розв'язок задачі:
# def menu_one():
#      if user_choise == "Відображення списку":
#          return print(new_list)
#      elif user_choise == "Отримання максимального значення у списку":
#          return print(max(new_list))
#      elif user_choise == "Отримання мінімального значення у списку":
#          return print(min(new_list))

# def menu_four():
#     try:
#         if index_from_list > quantity_elements :
#                   raise ValueError("користувач ввів неправильне значення для індексу елемента в списку")
#         return print(new_list[index_from_list - 1])
#     except ValueError as err:
#         return print("користувач ввів неправильне значення для індексу елемента в списку")

# def menu_five():
#     try:
#         if index_for_delete > quantity_elements :
#                   raise ValueError("користувач ввів неправильне значення для індексу елемента в списку")
#         del new_list[index_for_delete - 1]
#         return print(new_list)
#     except ValueError as err:
#         return print("користувач ввів неправильне значення для індексу елемента в списку")











#Завдання 2(b)
#Розв'язок завдання:
# def factorial():
#     try:
#         if user_number < 0 :
#             raise ValueError("Ви ввели від'ємне число")
#
#     except ValueError as err:
#         print(f"Помилка {err}")
#     else:
#         factorial = 1
#         for item in range(1, user_number + 1):
#                 factorial *= item
#         return print(f"Факторіал {user_number} = {factorial}")

#Завдання 2(a)
#Розв'язок завдання:
# def factorial():
#         factorial = 1
#         for item in range(1, user_number + 1):
#                 factorial *= item
#         return print(f"Факторіал {user_number} = {factorial}")






if __name__ == "__main__":
     print("Zdorov")

     #Завдання 1
     #Напишіть програму, яка запитує у користувача число і обчислює його факторіал.
     #Обробіть виняток, що виникає при введенні від'ємного числа, і виведіть повідомлення про помилку.



     #Розв'язок завдання:
     # try:
     #    user_number = int(input("Введіть число:"))
     #    if user_number < 0 :
     #        raise ValueError("Ви ввели від'ємне число")
     #
     # except ValueError as err:
     #    print(f"Помилка {err}")
     # else:
     #    factorial = 1
     #    for item in range(1, user_number + 1):
     #            factorial *= item
     #
     #
     #    print(f"Факторіал {user_number} = {factorial}")

     #Завдання 2
     #Реалізуйте перше завдання через функцію.
     #Функція повинна приймати число як параметр і повертати його факторіал.
     #Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:

        #a)Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
        #b)Друга версія обробляє виняток усередині функції.

     #Дані від користувача:
     # user_number = int(input("Введіть число:"))

     #Розв'язок 2(b):
     # print(factorial())

     # Розв'язок 2(a):
     # try:
     #     if user_number < 0:
     #         raise ValueError("Ви ввели від'ємне число")
     #
     # except ValueError as err:
     #     print(f"Помилка {err}")
     # else:
     #     print(factorial())

     #Завдання 3
     #Напишіть програму, яка дає змогу користувачеві заповнити список із клавіатури числами.
     #Після отримання даних відобразіть на екран меню, яке дозволяє виконати такі операції:
        #Відображення списку
        #Отримання максимального значення у списку;
        #Отримання мінімального значення у списку;
        #Відображення значення елемента за індексом, введеним користувачем;
        #Видалення елемента за індексом, введеним користувачем.
     #Обробіть виняток, що виникає під час виходу за межі списку
     #(користувач ввів неправильне значення для індексу елемента в списку), і виведіть повідомлення про помилку.

     #Дані від користувача:
     # new_list = []
     # while True:
     #     user_numbers = int(input("Введіть числа (для завершення процесу введіть 0):"))
     #     if user_numbers == 0:
     #            break
     #     new_list.append(user_numbers)
     #
     # quantity_elements = len(new_list)

     #Меню:
     # print("Виберіть необхідну операцію:\n1.Відображення списку\n2.Отримання максимального значення у списку\n3.Отримання мінімального значення у списку\n4.Відображення значення елемента за індексом, введеним користувачем\n5.Видалення елемента за індексом, введеним користувачем")
     # user_choise = input("Введіть потрібну вам операцію:")

     # try:
     #      if user_choise == "Відображення списку":
     #          print(new_list)
     #      elif user_choise == "Отримання максимального значення у списку":
     #          print(max(new_list))
     #      elif user_choise == "Отримання мінімального значення у списку":
     #          print(min(new_list))
     #      elif user_choise == "Відображення значення елемента за індексом, введеним користувачем":
     #          index_from_list = int(input("Введіть індекс зі списку який вас цікавить:"))
     #          if index_from_list > quantity_elements :
     #              raise ValueError("користувач ввів неправильне значення для індексу елемента в списку")
     #          print(new_list[index_from_list - 1])
     #      elif user_choise == "Видалення елемента за індексом, введеним користувачем":
     #          index_for_delete = int(input("Введіть індекс зі списку який вас цікавить:"))
     #          if index_for_delete > quantity_elements :
     #              raise ValueError("користувач ввів неправильне значення для індексу елемента в списку")
     #          del new_list[index_for_delete - 1]
     #          print(new_list)
     # except ValueError as err:
     #     print("користувач ввів неправильне значення для індексу елемента в списку")


     #Завдання 4
     #Реалізуйте третє завдання через функції. Створіть дві версії реалізації функцій:
     #a)Перша версія не обробляє винятки всередині функцій. Уся обробка знаходиться зовні;
     #b)Друга версія обробляє винятки всередині функцій.


     #Дані від користувача:
     # new_list = []
     # while True:
     #     user_numbers = int(input("Введіть числа (для завершення процесу введіть 0):"))
     #     if user_numbers == 0:
     #         break
     #     new_list.append(user_numbers)
     #
     # quantity_elements = len(new_list)

     # Меню:
     # print("Виберіть необхідну операцію:\n1.Відображення списку\n2.Отримання максимального значення у списку\n3.Отримання мінімального значення у списку\n4.Відображення значення елемента за індексом, введеним користувачем\n5.Видалення елемента за індексом, введеним користувачем")
     # user_choise = input("Введіть потрібну вам операцію:")

     #Розв'язок завдання 4(a)(НЕ ПРАЦЮЄ 4 і 5 КОМАНДА)!!!!!!!!!!:
     # if user_choise == "Відображення списку" or "Отримання максимального значення у списку" or "Отримання мінімального значення у списку":
     #         print(menu())
     # if user_choise == "Відображення значення елемента за індексом, введеним користувачем":
     #         index_from_list = int(input("Введіть індекс зі списку який вас цікавить:"))
     # try:
     #     if index_from_list > quantity_elements:
     #              raise ValueError("користувач ввів неправильне значення для індексу елемента в списку")
     #     else:
     #              print(menu())
     # except ValueError as err:
     #          print("користувач ввів неправильне значення для індексу елемента в списку")
     # try:
     #     if user_choise == "Видалення елемента за індексом, введеним користувачем":
     #        index_for_delete = int(input("Введіть індекс зі списку який вас цікавить:"))

     #     if index_for_delete > quantity_elements:
     #             raise ValueError("користувач ввів неправильне значення для індексу елемента в списку")
     #     else:
     #             print(menu())
     # except ValueError as err:
     #             print("користувач ввів неправильне значення для індексу елемента в списку")

     # Розв'язок завдання 4(b):
     # if user_choise == "Відображення списку" or "Отримання максимального значення у списку" or "Отримання мінімального значення у списку":
     #        print(menu_one())
     # if user_choise == "Відображення значення елемента за індексом, введеним користувачем":
     #     index_from_list = int(input("Введіть індекс зі списку який вас цікавить:"))
     #     print(menu_four())
     # if user_choise == "Видалення елемента за індексом, введеним користувачем":
     #     index_for_delete = int(input("Введіть індекс зі списку який вас цікавить:"))
     #     print(menu_five())