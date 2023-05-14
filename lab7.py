def proc1():
    from PIL import Image
    foto= Image.open("foto.JPG")
    foto.show()
    print("Размер изображения:", foto.size)
    print("Формат изображения:", foto.format)
    print("Цветовая модель:", foto.mode)

def proc2():
    from PIL import Image

    image = Image.open("foto.JPG")

    size = tuple([int(i / 3) for i in image.size])
    image.thumbnail(size)

    h_mirror = image.transpose(method=Image.FLIP_LEFT_RIGHT)

    v_mirror = image.transpose(method=Image.FLIP_TOP_BOTTOM)

    image.save("size.jpg")
    h_mirror.save("h_mirror.jpg")
    v_mirror.save("v_mirror.jpg")

def proc3():
    from PIL import  Image,ImageFilter
    import os
    try:
        os.mkdir("Vivod")
    except: FileExistsError
    for i in range(1,6):
        image = Image.open(f"{i}.jpg")
        image = image.filter(ImageFilter.DETAIL)
        image.save(f"Vivod/{i}_with_filter.jpg")

def proc4():
        from PIL import Image
        image = Image.open(f"1.jpg")
        watermark = Image.open("wm.png")
        watermark = watermark.resize((250,250))
        image.paste(watermark,(0,0), mask= watermark)
        image.show()




proc4()
    