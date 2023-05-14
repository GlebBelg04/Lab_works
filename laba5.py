import random
from random import randint


def proc1():
    my_list = [randint(1, 10) for i in range(randint(2, 12))]
    user_num = int(input("Угадайте число из списка: "))
    print(*my_list)
    print(user_num)
    if user_num in my_list:
        print("Вы угадали")
    else:
        print("В списке нет такого числа")


def proc2():
    my_list = [randint(1, 10) for i in range(randint(1, 10))]
    el = set(my_list)
    print(*my_list)
    for i in el:
        a = my_list.count(i)
        if a > 1:
            print(i, "встречается", a, "раз(a)")
    if len(my_list) == len(el):
        print("нет повторяющихся элементов")


def proc3():
    week = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    num = int(input("сколько выходных: "))
    print("Рабочие", *week[:-num])
    print("Выходные", *week[-num:])


def proc4():
    from random import sample
    my_gruppa = ["Иванов", "Смирнов", "Соболев", "Андреев", "Кузнецов"]
    gruppa2 = ["Стрельцов", "Батюченко", "Иванов", "Лопухов", "Сергеев"]
    sport = tuple(random.sample(my_gruppa, 3) + random.sample(gruppa2, 3))
    print("Моя группа: ", *my_gruppa)
    print("другая группа: ", *gruppa2)
    print(*sport, len(sport))
    if "Иванов" in sport:
        print("Фамилия Иванов входит в список секции столько раз:", sport.count("Иванов"))
    else:
        print("Иванова нет  в секции")


proc4()
