while(True):
    a = int(raw_input("1. sayiyi giriniz: "))
    b = int(raw_input("2. sayiyi giriniz: "))
    if a==b:
        print("A say�s� e�ittir B")
    elif a>b:
        print("A say�s� B say�s�ndan b�y�kt�r.")
    else:
        print("B say�s� A say�s�ndan b�y�kt�r.")
        break
