
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
            print("Yanlış tuşlama yaptınız", ex)
    else:
        break
    finally:
        print("try except sonlandı.")