bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))
bilangan3 = float(input("Masukkan bilangan ketiga: "))

if bilangan1 >= bilangan2 and bilangan1 >= bilangan3:
    bilangan_terbesar = bilangan1
elif bilangan2 >= bilangan1 and bilangan2 >= bilangan3:
    bilangan_terbesar = bilangan2
else:
    bilangan_terbesar = bilangan3

print("Bilangan terbesar adalah:", bilangan_terbesar)
