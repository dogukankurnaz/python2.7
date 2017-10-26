while(True):
    a = int(raw_input("1. Kenarý Giriniz : "))
    b = int(raw_input("2. Kenarý Giriniz : "))
    c = int(raw_input("3. Kenarý Giriniz : "))
    if a==b and b==c :
        print("Eþkenar Üçgen")
    elif a==b or b==c or a==c:
        print("Ýkizkenar Üçgen")
    else:
        print("Çeþitkenar Üçgen")
       
        
    
