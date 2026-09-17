# Buat file dengan nama Logika_2611532022.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan input ()
# Program operator logika dalah Phyton

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2022 = input("Masukkan nilai boolean-1_2022 (True/False):")
a2_2022 = input("Masukkan nilai boolean-2_2022 (True/False):")

print("\nA1_2022 =", a1_2022)
print("A2_2022 =", a2_2022)

# Konjungsi: bernilai True jika keduanya True
hasil = a1_2022 and a2_2022
print("\nKonjungsi (AND):")
print("A1_2022 and A2_2022 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1_2022 or a2_2022
print("\nDisjungsi (OR):")
print("A1_2022 or A2_2022 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1_2022
print("\nNegasi A1_2022 (NOT):")
print(" not A1_2022 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2_2022
print("\nNegasi A2_2022 (NOT):")
print(" not A2_2022 =", hasil)

# XOR: bernilai True jika nilai keduanya berbeda
hasil = a1_2022 != a2_2022
print("\nDisjungsi Ekslusif (XOR):")
print("A1_2022 XOR A2_2022 =", hasil)