#Buat file dengan nama Konstanta_2611532022.py
#Program ini menggunakan konstanta untuk menghitung luas lingkaran
#Nama variable ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI : Final = 3.14
print("pi: %f" % (PI))
jari_2022 = float(input("Masukkan nilai jari-jari: "))
luas_2022 = PI * jari_2022 * jari_2022
print("luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2022, luas_2022))