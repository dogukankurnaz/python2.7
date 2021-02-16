def binary(c):
    print "{0:b}".format(c),

cumle=raw_input("Cevrilmesi istediginiz yaziyi giriniz:  ")
for i in cumle:
   asc=ord(i)
   binary(asc)
