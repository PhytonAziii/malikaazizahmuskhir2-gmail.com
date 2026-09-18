# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2022 = int(input("Input angka-1: "))
angka2_2022 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_2022 = angka1_2022 > angka2_2022
print("\nOperator lebih besar dari")
print("angka1_2022 > angka2_2022 =",hasil_2022)

# Lebih kecil dari
hasil_2022 = angka1_2022 < angka2_2022
print("\nOperator lebih kecil dari")
print("angka1_2022 < angka2_2022 =",hasil_2022)

# Lebih besar dari atau sama dengan
hasil_2022 = angka1_2022 >= angka2_2022
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2022 >= angka2_2022 =",hasil_2022)

# Lebih kecil dari atau sama dengan
hasil_2022 = angka1_2022 <= angka2_2022
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_2022 <= angka2_2022 =",hasil_2022)

# Sama dengan
hasil_2022 = angka1_2022 == angka2_2022
print("\nOperator sama dengan")
print("angka1_2022 == angka2_2022 =",hasil_2022)

# Tidak sama dengan
hasil_2022 = angka1_2022 != angka2_2022
print("\nOperator tidak sama dengan")
print("angka1_2022 != angka2_2022 =",hasil_2022)

# Tambahan: perbandingan berantai dalam Python
hasil_2022 = 0 < angka1_2022 < 100
print("\nPerbandingan berantai")
print("0 < angka1_1022 < 100 =",hasil_2022)

hasil_2022 = 0 < angka2_2022 < 100
print("0 < angka2_1022 < 100 =",hasil_2022)
