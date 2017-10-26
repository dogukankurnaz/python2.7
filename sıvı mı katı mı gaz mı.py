while(True):
    s = int(raw_input("Sýcaklýk deðerini giriniz: "))
    if s<0:
        print("katý")
    elif s>0 and s<100:
        print("sývý")
    else:
        print("gaz")
    
