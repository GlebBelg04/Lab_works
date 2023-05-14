def proc1():

    import json

    with open('data.json', encoding= "utf-8") as f:
        data = json.load(f)

    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    available = input("Товар в наличии? (да/нет): ").lower() == "да"
    weight = int(input("Введите вес продукта: "))


    new_product = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }
    data['products'].append(new_product)


    with open('data.json', 'w') as f:
        json.dump(data, f)

    print("\nОбновленные данные:")
    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

def proc2():

    with open('en-ru.txt', encoding= "utf-8") as f:
        data = f.read().strip().split('\n')

    ru_en = {}

    for line in data:
        words = line.split(' - ')

        english_word = words[0]
        russian_words = words[1].split(', ')

        for russian_word in russian_words:
            if russian_word not in ru_en:
                ru_en[russian_word] = [english_word]
            else:
                ru_en[russian_word].append(english_word)

    sorted_keys = sorted(ru_en.keys())

    with open('ru-en.txt', 'w') as f:
        for key in sorted_keys:
            english_words = ', '.join(ru_en[key])
            f.write(f"{key} - {english_words}\n")

proc2()