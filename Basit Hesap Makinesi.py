a = int(input("Sayıyı giriniz:"))
b = int(input("Sayıyı giriniz:"))

islem = input("İşlem Giriniz:")

if islem == "1":
    print("{} + {} = {}".format(a,b,a+b))
elif islem == "2":
    print("{} - {} = {}".format(a,b,a-b))
elif islem == "3":
    print("{} * {} = {}".format(a,b,a*b))
elif islem == "4":
    print("{} / {} = {}".format(a,b,a/b))
    