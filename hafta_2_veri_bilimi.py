# -*- coding: utf-8 -*-
# Ödev: Yaz Kampı - Veri Bilimi Hafta 2

# Soru 1 - Sayı Analizi
sayi = int(input("Bir sayı giriniz: "))
if sayi > 0:
    durum = "Pozitif"
elif sayi < 0:
    durum = "Negatif"
else:
    durum = "Sıfır"

tekcift = "Çift" if sayi % 2 == 0 else "Tek"
print(f"{durum} {tekcift}")

# Soru 2 - Harf Frekansı
kelime = input("Bir kelime giriniz: ")
frekans = {}
for harf in kelime:
    frekans[harf] = frekans.get(harf, 0) + 1
print(frekans)

# Soru 3 - Şifre Kontrolü
sifre = input("Şifre giriniz: ")
if len(sifre) < 8:
    print("Şifre en az 8 karakter olmalı.")
elif not any(harf.isupper() for harf in sifre):
    print("Şifre en az bir büyük harf içermeli.")
elif not any(harf.isdigit() for harf in sifre):
    print("Şifre en az bir rakam içermeli.")
else:
    print("Şifre geçerli!")

# Soru 4 - Liste İşlemleri
sayilar = [12, 4, 9, 25, 30, 7, 18]
ortalama = sum(sayilar)/len(sayilar)
buyukler = [s for s in sayilar if s > ortalama]
print("Ortalama:", ortalama)
print("Ortalamadan büyük sayılar:", buyukler)

# Soru 5 - Nested Loop (Desen)
for i in range(1,6):
    print('*'*i)

# Soru 6 - While Döngüsü
toplam = 0
adet = 0
while True:
    sayi = int(input("Sayı giriniz (0 çıkış): "))
    if sayi == 0:
        break
    toplam += sayi
    adet += 1
if adet > 0:
    print("Toplam:", toplam)
    print("Ortalama:", toplam/adet)
else:
    print("Hiç sayı girilmedi.")

# Soru 7 - Palindrom Kontrolü
kelime = input("Bir kelime giriniz: ")
if kelime == kelime[::-1]:
    print("Palindrom")
else:
    print("Değil")

# Soru 8 - List Comprehension
liste = [x**2 for x in range(1,101) if x%3==0 and x%5==0]
print(liste)

# Soru 9 - String İşlemleri
cumle = input("Bir cümle giriniz: ")
kelimeler = cumle.split()
yeni = ' '.join([kelime.capitalize() for kelime in kelimeler])
print(yeni)

# Mini Proje - Film Yorumu Analizi
yorumlar = []
n = int(input("Kaç yorum gireceksiniz? "))
for i in range(n):
    yorum = input(f"{i+1}. yorumu giriniz: ")
    yorumlar.append(yorum)
uzunluklar = [len(y) for y in yorumlar]
yi_sayisi = sum('iyi' in y.lower() for y in yorumlar)
en_uzun = max(yorumlar, key=len)
en_kisa = min(yorumlar, key=len)
ortalama_uz = sum(uzunluklar)/len(yorumlar)
print("Toplam yorum sayısı:", len(yorumlar))
print('"iyi" geçen yorum sayısı:', iyi_sayisi)
print("En uzun yorum:", en_uzun)
print("En kısa yorum:", en_kisa)
print("Ortalama uzunluk:", ortalama_uz, "karakter")
