import tkinter


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


class iceCream(restaurant):

    def __init__(self, name, type):
        super().__init__(name, type)

    flavors = ["Пломбир", "Ваниль", "Фруктовое"]
    place = "Большая Морская улица д.18"
    time = ["10:00", "20:00"]
    types = ["мороженое на палочке", "мягкое мороженое", "Стаканчик"]

    def flavors_show(self):
        print(*self.flavors)

    def flavors_add(self):
        self.flavors.append(input("Добавить вкус: "))

    def flavors_remove(self, x):
        if x in self.flavors:
            self.flavors.remove(x)

    def flavors_avaible(self):
        x = input("поиск вкуса: ")
        if x in self.flavors:
            print("Avaible")
        else:
            print("unavaible")

    def types_show(self):
        print(*self.types)

    def zakaz(self, type, flavor):
        if type in self.types and flavor in self.flavors:
            print(f"Вы заказали {type} со вкусом {flavor}")
        else:
            print("сожалению такого нет в меню")


icer = iceCream("Мороженщик", "мороженница")

icer.flavors_show()
icer.describe_restaurant()
print(icer.time)
icer.flavors_add()
icer.flavors.remove("Пломбир")
icer.flavors_show()
icer.flavors_avaible()
icer.zakaz(input("Вид мороженного: "),input(": "))

window = tkinter.Tk()
window.title(icer.restaurant_name)
lbl = tkinter.Label(window, text="Avaible flavors")
lbl.grid(column=0, row=0)
lbl2 = tkinter.Listbox(width=15, height=8)
lbl2.grid(column=0, row=1)
for i in icer.flavors:
    lbl2.insert(0, i)

window.mainloop()
