print("Sayıları giriniz!!!")

a = float(input("Sayı giriniz:"))
b = float(input("Sayı giriniz:"))
c = float(input("Sayı giriniz:"))

if a>b and a>c:
    print("En büyük sayı:",a)
elif b>a and b>c:
    print("En büyük sayı:",b)
elif c>a and c>b:
    print("En büyük sayı:",c)