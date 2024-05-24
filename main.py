harfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
liste1 = []
kelime_ekle = input("kelime giriniz: ")
liste1.append(kelime_ekle)
print("yeni listeniz oluşturuldu.")

sesli_harf_var = any(harf in kelime_ekle for harf in harfler)

if sesli_harf_var:
    print("kelimenizde sesli harf bulunmaktadır.")
else:
    print("kelimenizde sesli harf bulunmamaktadır.")
