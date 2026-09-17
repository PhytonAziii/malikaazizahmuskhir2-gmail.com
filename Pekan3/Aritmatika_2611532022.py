# Buat file dengan nama aritmatika_2611532022.py
# Buat program untuk operator arotmatika dalam phyton
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2022 = int(input("input angka-1:"))
angka2_2022 = int(input("input angka-2:"))

# penjumlahan
hasil = angka1_2022 + angka2_2022
print("\nOperator Penjumlahan:")
print("Hasil =", hasil)

# pengurangan
hasil = angka1_2022 - angka2_2022
print("\nOperator Pengurangan:")
print("Hasil =", hasil)

# perkalian
hasil = angka1_2022 * angka2_2022
print("\nOperator Perkalian:")
print("Hasil =", hasil)

# pembagian
if angka2_2022 != 0:
    hasil = angka1_2022 / angka2_2022
    print("\nOperator Pembagian:")
    print("Hasil =", hasil)

    hasil = angka1_2022 // angka2_2022
    print("\nOperasi Pembagian Bulat:")
    print("Hasil =", hasil)

    hasil = angka1_2022 % angka2_2022
    print("\nOperator Sisa Bagi:")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak boleh bernilai 0")

# Pangkat
hasil = angka1_2022 ** angka2_2022
print("\nOperator Pangkat:")
print("Hasil =", hasil)
