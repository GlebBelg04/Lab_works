N = int(input())
words = ""
for i in range(N):
    word = str(input())
    words += word + " "

print(words)

def proc1 ():
    word = str (input())
    words = ""
    while word != "stop":
        words += word + " "
        word = str(input())
    print(words)

def proc2 ():
    while ( word := str(input())) != "stop" :
        if "ф" in word or "Ф" in word :
            print("Ого, это редкое слово")
        else:
            print("Эх, жаль но это не редкое слово")

def proc3 ():
    from random import randint
    health = 3
    while True :
        a = randint(1,100)
        b = randint(1,100)
        print(f"{a} + {b} = ",end="")
        res = input()
        while not res.isdigit() and res != "stop":
            print("error",end="")
            res = input()
        if res == "stop":
            break
        if health == 0 :
            break
        if int(res) == a+b :
            print("Верно")
        else:
            print("Неверно")
            health -= 1
proc1(),proc2(),proc3()