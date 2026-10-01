# Buat nama file dengan nama perulangan_for1_2611532022.py
# Buat program utuk perulangan for dalam phyton
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakn fungsi input()

ulang_2022 = int(input("Masukkan jumlah perulangan :"))

jumlah_2022 = 0
for i_2022 in range(1, ulang_2022 + 1):
   print(i_2022, end=" ")
   jumlah_2022 = jumlah_2022 + i_2022

if i_2022 < ulang_2022:
  print("+", end=" ")
else:
   print("=", jumlah_2022, end=" ")

print()
print("Jumlah_2022 = ", jumlah_2022)
