vize1 = int(input("Vize 1 notunuzu girin:"))
vize2 = int(input("Vize 2 notunuzu girin:"))
final = int(input("Final notunuzu girin:"))

toplam_not=(vize1*30/100)+(vize2*30/100)+(final*40/100)

if toplam_not>=90:
    print("Alınan harf notu:AA")
elif toplam_not>=85:
    print("Alınan harf notu:BA")
elif toplam_not>=80:
    print("Alınan harf notu:BB")
elif toplam_not>=75:
    print("Alınan harf notu:CB")
elif toplam_not>=70:
    print("Alınan harf notu:CC")
elif toplam_not>=65:
    print("Alınan harf notu:DC")
elif toplam_not>=60:
    print("Alınan harf notu:DD")
elif toplam_not>=55:
    print("Alınan harf notu:FD")
elif toplam_not<55:
    print("Alınan harf notu:FF")
