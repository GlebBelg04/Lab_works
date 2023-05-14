class restaurant:

    restaurant_rating = 0

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("ресторан открыт")

    def rating(self):
        print("Текущий рейтинг (0-10):", self.restaurant_rating)
        self.restaurant_rating = int(input("Введите рейтинг: "))
        if self.restaurant_rating > 10:
            self.restaurant_rating = 10
        if self.restaurant_rating < 0:
            self.restaurant_rating = 0
        print("Обновленный рейтинг (0-10):", self.restaurant_rating)


newReustarant = restaurant("Виктор", "Французская")
print(newReustarant.restaurant_name)
print(newReustarant.cuisine_type)
print()
newReustarant.describe_restaurant()
print()
newReustarant.open_restaurant()
print()
Mone = restaurant("Моне", "Французская")
sushi_bar = restaurant("Суши бар", "Азиатская")
Borsch = restaurant("Борщ", "Русская")
Mone.describe_restaurant()
sushi_bar.describe_restaurant()
Borsch.describe_restaurant()

Mone.rating()
