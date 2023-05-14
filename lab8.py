def proc1():
    from PIL import Image
    image = Image.open('card.jpg')
    crop_area = (image.width/2, image.height/2, image.width, image.height)
    cropped_image = image.crop(crop_area)
    cropped_image.save('cropped_card.jpg')

def proc2():
    from PIL import Image
    cards = {
        'День рождения': 'birthday.jpg',
        'День Святого Валентина': 'valentine.jpg',
        'Новый год': 'new_year.jpg'
    }
    holiday = input('Введите название праздника: ')
    card_name = cards.get(holiday)

    if card_name is None:
        print('Открытка не найдена')
    else:
        image = Image.open(card_name)
        image.show()

def proc3():
    from PIL import Image, ImageDraw, ImageFont

    image = Image.open('card.jpg')

    crop_area = (image.width/2, image.height/2, image.width, image.height)

    cropped_image = image.crop(crop_area)

    name = str(input('Введите имя человека, которого вы хотите поздравить: '))

    name = name + ", Поздравляю"

    draw = ImageDraw.Draw(cropped_image)

    font = ImageFont.truetype('arial.ttf', size=50)

    draw.text((60,30), name, font= font, fill= "red", stroke_width=2, stroke_fill="red" )

    cropped_image.show()

    cropped_image.save("cropped.png")



proc2()


