while(True):
    a = int(raw_input("1. sayiyi giriniz: "))
    b = int(raw_input("2. sayiyi giriniz: "))
    if a==b:
        print("A sayısı eşittir B")
    elif a>b:
        print("A sayısı B sayısından büyüktür.")
    else:
        print("B sayısı A sayısından büyüktür.")
        break
