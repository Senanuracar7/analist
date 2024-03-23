print("Ödev Tamamlandı")

#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
fibonacci = [1, 1]  # İlk iki elemanı 1'e eşit olan Fibonacci serisi

while len(fibonacci) < 20:  # En az 20 elemanlı olacak şekilde döngü
  next_number = fibonacci[-1] + fibonacci[-2]  # Son iki elemanın toplamı
fibonacci.append(next_number)  # Yeni sayıyı listeye ekle

print(fibonacci)


#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
#Mükemmel sayı, kendisi dışındaki bölenlerinin toplamı kendisine eşit olan sayılara denir. Örneğin 6 mükemmel sayıdır. 
#6'nın kendisi dışındaki bölenleri {1, 2, 3}'tür ve 1 + 2 + 3 yine 6'ya eşit olur.

sayi=int(input("Bir Sayı Giriniz: "))
toplam = 0
for i in range(1,sayi):
    if sayi%i == 0:
         toplam+=i
if toplam == sayi:
 print("Sayi Mükemmel Sayıdır")   
else : 
    print("Sayi Mükemmel Değildir")   


#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

def ebob(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# EKOK hesaplama fonksiyonu
def ekok(a, b):
    return a * b // ebob(a, b)

# Kullanıcıdan sayıları al
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# EBOB ve EKOK'u hesapla
ebob_sonucu = ebob(sayi1, sayi2)
ekok_sonucu = ekok(sayi1, sayi2)

# Sonuçları ekrana yazdır
print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {ebob_sonucu}")
print(f"{sayi1} ve {sayi2} sayılarının EKOK'u: {ekok_sonucu}")

#Bu çıktıda, girilen sayılar olan 12 ve 18'in EBOB'u 6'dır 
#çünkü 12'nin bölenleri {1, 2, 3, 4, 6, 12} ve
#18'in bölenleri {1, 2, 3, 6, 9, 18} ve 
#en büyük ortak bölen bu kümelerin kesişiminde yer alır. 
#EKOK ise 36'dır çünkü 12 ve 18'in ortak katlarının içinde en küçük olanıdır.
    

#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
sayi=int(input("Sayıyı Girin : "))
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi," Asal Sayı Değildir.")
           break
   else:
       print(sayi," Asal Sayıdır.")
 
else:
   print(sayi," Asal Sayı Değildir.")
 


#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

def asal_carpanlar(sayi):
    carpanlar = []
    carpan = 2

    while sayi > 1:
        while sayi % carpan == 0:
            carpanlar.append(carpan)
            sayi //= carpan
        carpan += 1

    return carpanlar

sayi = int(input("Bir sayı girin: "))

print(f"{sayi}'nin asal çarpanları: {asal_carpanlar(sayi)}")