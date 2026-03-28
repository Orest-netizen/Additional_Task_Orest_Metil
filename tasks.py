# #Завдання 1
# languages = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]
# print("Оригінальний список:", languages)
# print("Тимчасово відсортований (sorted):", sorted(languages))
# print("Список після sorted (не змінився):", languages)
# languages.reverse()
# print("Список після reverse():", languages)
# languages.sort()
# print("Список після sort() (алфавітний порядок):", languages)
#
# #Завдання 2
# input_string = input("Введіть цілі числа через пробіл: ")
# numbers = [int(x) for x in input_string.split()]
# print("Сума чисел:", sum(numbers))
#
# #Завдання 3
# cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
# result = ", ".join(cities[:-1]) + " and " + cities[-1]
# print(result)
#
# #Завдання 4
# digits = input("Введіть 5 цифр через пробіл:").split()
# new_list = sorted(digits, reverse=True)
# print("".join(new_list))
#
#Завдання 5
professions = ["Doctor", "Engineer", "Teacher"]
professions.append("Designer")
professions.insert(1, "Pilot")
print(f"Кількість професій у списку: {len(professions)}")
removed = professions.pop(2)
print(f"Видалено: {removed}")
professions.remove("Doctor")
professions.sort()
print("Фінальний список:", professions)
#
# #Завдання 6
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