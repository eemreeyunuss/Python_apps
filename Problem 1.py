print("..............////Beden Kitle Endeksi Hesabı////.............")


boy=float(input("Boyunuzu giriniz:"))

kilo=int(input("Kilonuzu giriniz:"))


bki= kilo / (boy * boy)

if bki<18.5:
    print("zayif")
elif bki>=18.5 and bki<25:
    print("normal")
elif bki>=25 and bki<30:
    print("fazla kilolu")
elif bki>=30:
    print("obez")