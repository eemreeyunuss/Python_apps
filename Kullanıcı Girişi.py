print("Kullanıcı bilgileri giriş sistemine hoşgelidiniz.")

kullanıcı_adı = "karaemreyunus"
kullanıcı_sifre = "07919610"

kullanıcı_adı_giris = input("Kullanıcı adını giriniz:")
kullanıcı_sifre_giris = input("Kullanıcı sifresi giriniz:")

if kullanıcı_adı == kullanıcı_sifre_giris and kullanıcı_sifre == kullanıcı_sifre_giris:
    print("Giriş yapılıyor....")
elif kullanıcı_adı != kullanıcı_adı_giris and kullanıcı_sifre == kullanıcı_sifre_giris:
    print("Kullanıcı adı hatalı!!!!")
elif kullanıcı_adı == kullanıcı_adı_giris and kullanıcı_sifre != kullanıcı_sifre_giris:
    print("Kullanıcı sifresi hatalı!!!!")
else:
    print("Kullanıcı adı ve sifresi hatalı!!!!!")