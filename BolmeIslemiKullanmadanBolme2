bolum = 1
def bolme(bolunen, bolen):
    global bolum
    kalan = bolunen - bolen
    if kalan >= bolen:
        bolum += 1
        return bolme(kalan, bolen)
    else:
        return "{}.{}".format(bolum, kalan) #format komutu 15'i 3 e bolecek ve 3.1 yazacak eger noktayi silersek ve onun yerine , koyarsak 3,1 yazacak.
print bolme(15, 3)
