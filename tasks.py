# #Вправа 1
# names = ['Анна', 'Максим', 'Олена', 'Ігор']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
#
# #Вправа 2
# transport = ['мотоцикл', 'велосипед', 'автомобіль']
# print(f"Я хотів би купити {transport[1]}.")
#
# #Вправа 3
# years_list = [2000, 2001, 2002, 2003, 2004, 2005]
# print(f"Мені виповнилося 3 роки у {years_list[3]} році.")
# years_list.append(2006)
# print("Оновлений список:", years_list)
# print(f"Найбільше років мені було у {years_list[-1]} році.")
#
# #Вправа 4
# things = ['wallet', 'mirror', 'umbrella']
# print(things[2].capitalize())
# print("Список після capitalize (не змінений):", things)
# things[2] = things[2].upper()
# print("Список після upper():", things)
# things.remove('UMBRELLA')
# print("Список після видалення:", things)
#
# #Вправа 5
# languages = ['Georgian', 'Estonian', 'Ukrainian']
# last_lang = languages[-1].lower()
# print(last_lang)
# reversed_lang = last_lang[::-1].capitalize()
# print(reversed_lang)
#
# #Вправа 6
# hardware = ('CPU', 'RAM', 'SSD')
# software = ['Python', 'Linux', 'VS Code']
# print("Hardware:", hardware)
# print("Software:", software)
# software[0] = 'C++'
# print("Оновлений Software:", software)

# #Задача 1
# languages = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]
# print("Оригінальний список:", languages)
# print("Тимчасово відсортований (sorted):", sorted(languages))
# print("Список після sorted (не змінився):", languages)
# languages.reverse()
# print("Список після reverse():", languages)
# languages.sort()
# print("Список після sort() (алфавітний порядок):", languages)
#
# #Задача 2
# input_string = input("Введіть цілі числа через пробіл: ")
# numbers = [int(x) for x in input_string.split()]
# print("Сума чисел:", sum(numbers))
#
# #Задача 3
# cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
# result = ", ".join(cities[:-1]) + " and " + cities[-1]
# print(result)
#
# #Задача 4
# digits = input("Введіть 5 цифр через пробіл:").split()
# new_list = sorted(digits, reverse=True)
# print("".join(new_list))
#
# #Задача 5
# professions = ["Doctor", "Engineer", "Teacher"]
# professions.append("Designer")
# professions.insert(1, "Pilot")
# print(f"Кількість професій у списку: {len(professions)}")
# removed = professions.pop(2)
# print(f"Видалено: {removed}")
# professions.remove("Doctor")
# professions.sort()
# print("Фінальний список:", professions)
#
# #Задача 6
# keywords = ('for', 'if', 'else', 'in', ':')
# indent = "    "
# line1 = f"{keywords[0]} each token {keywords[3]} the postfix expression {keywords[4]}"
# line2 = f"{indent}{keywords[1]} the token is a number {keywords[4]}"
# line3 = f"{indent * 2}print('Convert it to an integer and add it to the end of values')"
# line4 = f"{indent}{keywords[2]}"
# line5 = f"{indent * 2}print('Append the result to the end of values')"
# print(line1)
# print(line2)
# print(line3)
# print(line4)
# print(line5)