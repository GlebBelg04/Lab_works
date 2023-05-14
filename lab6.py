def proc1():
    capitals = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага",
                "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                "Северная Македония": "Скопье", "Сербия": "Белград"}

    for key in capitals:
        print(key, "-", capitals[key])

    input()
    country = input("Введите страну: ")
    try:
        print(capitals[country])
    except:
        KeyError
        print("Такой страны нет в списке")

    input()
    l = [i for i in capitals.keys()]
    l.sort()
    for i in l:
        print(i, capitals[i])


def proc2():
    letter_values = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }

    word = input("Введите слово: ").upper()
    score = 0

    for letter in word:
        score += letter_values.get(letter, 0)

    print("Стоимость слова", word, ":", score)

def proc3():
    students = {"Иван":["Китайский","Русский","Английский"],
                "Игорь":["Русский","Немецкий","Французский"],
                "Максим":["Русский","Французский"],
                "Илья":["Русский","Китайский","Французский"],
                "Глеб":["Русский","Китайский"],
                "Никита":["Русский","Французский","Немецкий"],}
    language = []
    for i in students.values():
        for j in i:
            language.append(j)
    language = list(set(language))
    language.sort()
    chinese = []
    for key,value in students.items():
        if "Китайский" in value :
            chinese.append(key)
    print(*language)
    print(*chinese)
proc1(), proc2(), proc3()

