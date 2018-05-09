#coding:utf-8
sayi1=int(raw_input("Sayi 1'i giriniz:"))
sayi2=int(raw_input("Sayi 2'yi giriniz:"))
def bol(sayi1,sayi2,kalan,bolme):
    if kalan==0:
        bolme=sayi1
    if bolme>=sayi2:
        bolme -= sayi2
        kalan+=1
        bol(sayi1,sayi2,kalan,bolme)

    elif bolme>0:
        bolnoktalisayi(bolme,kalan,sayi1,sayi2,0)
    else:
        print kalan

def bolnoktalisayi(kalan,sonuc,sayi1,sayi2,sayac):
    bolme=sayi1
    if sayac==0:
        bolme=kalan*10
        kalan=0
    sayac+=1
    if bolme>=sayi2:
        bolme -=sayi2
        kalan+=1
        bolnoktalisayi(kalan,sonuc,bolme,sayi2,sayac)
    else:
        strsonuc=""
        if bolme>0:
            strsonuc+="<= Sonuç"
        print str(sonuc)+","+str(kalan)+strsonuc
bol(sayi1,sayi2,0,sayi1)
