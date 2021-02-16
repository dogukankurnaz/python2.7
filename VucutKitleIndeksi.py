#coding:utf-8
print "Hoşgeldiniz"
boy=float(raw_input("Lütfen Boyunuzu(m) giriniz: "))
kilo=int(raw_input("Lütfen Kilonuzu(kg) giriniz: "))
boy_kilo_index=kilo/boy**2
if(boy_kilo_index<=1.80):
    print "Zayıfsınız"
elif(boy_kilo_index<=25.0):
    print "Normalsiniz"
elif(boy_kilo_index<=30.0):
    print "Kilolusunuz"
elif(boy_kilo_index<=35.0):
    print "1.dereceden obezsiniz"
elif(boy_kilo_index<=40.0):
    print "2.dereceden obezsiniz"
elif(boy_kilo_index >= 40.0):
    print "3.dereceden obezsiniz"
