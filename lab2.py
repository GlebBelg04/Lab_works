passord_1 = input()
password_aprove = input()
if passord_1 == password_aprove :
    print("Пароль принят")
else:
    print("Пароль не принят")
def year (a):
    if (a%4 == 0 and a%100 != 0) or a%400 == 0 :
        print("Год ",a," - високосный")
    else:
        print("Этот год не високосный")

def proc1 ():
    colors = ["красный","синий","желтый"]
    while True :
        color1 = input()
        if color1 in colors:
            break
        print("Это не основной цвет, введите другое слово")
    while True :
        color2 = input()
        if color2 in colors:
            break
        print("Это не основной цвет, введите другое слово")
    colors = [color1,color2]
    if "красный" in colors and "синий" in colors:
        print("фиолетовый")
    if "красный" in colors and "желтый" in colors:
        print("оранжевый")
    if "желтый" in colors and "синий" in colors:
        print("зеленый")
year(2023),proc1()

