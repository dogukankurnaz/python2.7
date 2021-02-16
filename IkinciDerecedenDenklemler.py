while(True):
    a = int(raw_input("a sayisini giriniz: "))
    b = int(raw_input("b sayisini giriniz: "))
    c = int(raw_input("c sayisini giriniz: "))
    D = b*b-4*a*c
    X1 = (-1*b+D**1/2)/(2*a)
    X2 = (-1*b-D**1/2)/(2*a)
    if D<0:
        print("Kokler Sanal")
    else:
        print(X1,X2)
    
