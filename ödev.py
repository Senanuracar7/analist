print("Merhaba Kullanıcı")


#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy  = float(input('Lütfen boyunuzu "metre" cinsinden giriniz...'))
kilo = float(input('Lütfen kilonuzu "kilogram" cinsinden giriniz...'))
VKİ= kilo / (boy * boy)
print("Vücut Kitle Endeksiniz", VKİ)


#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
Güncelmaas=0
maas=input("Mevcut Maasi Gir : ")
zam=input("Zam Oranı(%) : ")
Güncelmaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamli Maaş :",Güncelmaas)
 

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayi1 = int(input("Lütfen Birinci Sayıyı Giriniz: "))
sayi2 = int(input("Lütfen İkinci Sayıyı Giriniz: "))
sayi3 = int(input("Lütfen Üçüncü Sayıyı Giriniz: "))

enBuyuk = max(sayi1, sayi2, sayi3)
print("En büyük değer:", enBuyuk)
 


#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
yariçap= input(str("Lütfen dairenin yariçapini giriniz: "))
Çevre = 2 * 3 * float (yariçap)
alan= 3 * float (yariçap) * float (yariçap)
print("Dairenin Alanı", alan)
print("Dairenin Çevresi", Çevre)


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
for i in range(100,1000):
    s = str(i)
    t = s[::-1]
    if s == t:
        print(s)