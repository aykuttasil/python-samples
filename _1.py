ad = "aykut"
print(ad)

# lower - upper
ad = "aykut".upper()
print(ad)

ad = ad.lower()
print(ad)

# len
print("Ad uzunluğu:" + str(len(ad)))

# substring
print(ad[1:2])  # 1. karakterden 2. karaktere kadar substring. 2 dahil değil
print(ad[2:])  # 2. karakterden sonuna kadar substring
print(ad[:2])  # baştan 2. karakter kadar substring

# replace
print(ad.replace("a", "O"))

# split & strip
cumle = "2020 hedeflerim arasında Python öğrenmek var.  "
# default olarak strip() ile baştaki ve sondaki boşlukları temizleyip,
# boşluk karakterine göre split eder.
print(cumle.split())
arr = cumle.split(" ")
print(arr)

cumle = cumle.strip()
arr = cumle.split(" ")
print(arr)


# input

username = input("username: ")
print(username)

sayi1 = input("Sayi1: ")
sayi2 = input("Sayi2: ")
print("Toplam:" + str((int(sayi1) + int(sayi2))))


################