# Buat file dengan nama assignment_2611532022.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Phyton

angka1_2022 = int(input("input angka-1_2022: "))
angka2_2022 = int(input("input angka-2_2022: "))

print("\nNilai awal angka1_2022 =", angka1_2022)
print("Nilai awal angka2_2022 =", angka2_2022)

# Assignment biasa
hasil = angka1_2022
print("\nAssignment biasa:")
print("hasil =", hasil)

# Assignment penambahan
hasil = angka1_2022
hasil += angka2_2022
print("\nAssignment penambahan (+=):")
print("hasil =", hasil)

# Assignment pengurangan
hasil = angka1_2022
hasil -= angka2_2022
print("\nAssignment pengurangan (-=):")
print("hasil =", hasil)

# Assignment perkalian
hasil = angka1_2022
hasil *= angka2_2022
print("\nAssignment perkalian (*=):")
print("hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2022 !=0:
    hasil = angka1_2022
    hasil /= angka2_2022
    print("\nAssignment pembagian (/=):")
    print("hasil =", hasil)
    # Operator tambahan
    hasil = angka1_2022
    hasil //= angka2_2022
    print("\nAssignment pembagian bulat (//=):")
    print("hasil =", hasil)
    # Sisa bagi
    hasil = angka1_2022
    hasil %= angka2_2022
    print("\nAssignment sisa bagi (%=):")
    print("hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0")

# Operator tambahan: assignment perpangkatan
hasil = angka1_2022
hasil **= angka2_2022
print("\nAssignment perpangkatan (**=):")
print("hasil =", hasil)
