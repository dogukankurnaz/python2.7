while(True):
    a = int(raw_input("1. Kenar� Giriniz : "))
    b = int(raw_input("2. Kenar� Giriniz : "))
    c = int(raw_input("3. Kenar� Giriniz : "))
    if a==b and b==c :
        print("E�kenar ��gen")
    elif a==b or b==c or a==c:
        print("�kizkenar ��gen")
    else:
        print("�e�itkenar ��gen")
       
        
    
