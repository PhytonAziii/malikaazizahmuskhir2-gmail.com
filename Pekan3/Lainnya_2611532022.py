# Buat file dengan nama Lainnya_2611532022.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Program operator keanggotan dan identitas

print("===========================================")
print("1. Operator Keanggotaan")
print("===========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data = input("Masukkan beberapa angka, pisahkan dengan koma:")

# Mengubah input menjadi list integer
data = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("Masukkan nilai yang dicari:"))

# Operator in
hasil = nilai_dicari in data
print("\nOperator keanggotaan IN")
print("nilai_dicari, "in" data =", hasil)

# Operator not in
hasil = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN")
print("nilai_dicari, "not in" data =", hasil)

print("\n===========================================")
print("2. Operator Identitas")
print("===========================================")

# objek1_2022 menggunakan list dari input pengguna
objek1_2022 = data

# objek2_2022 menggunakan list yang sama dengan objek1_2022
objek2_2022 = objek1_2022

# objek3_2022 menmiliki isi yang sama, tetapi merupakan objek yang berbeda
objek3_2022 = data.copy()

print("objek1_2022 =", objek1_2022)
print("objek2_2022 =", objek2_2022)
print("objek3_2022 =", objek3_2022)

#operator is
hasil = objek1_2022 is objek2_2022
print("\nOperator identotas IS")
print("objek1_2022 is objek2_2022 =", hasil)

#operator is not 
hasil = objek1_2022 is not objek3_2022
print("\nOperator identotas IS NOT")
print("objek1_2022 is not objek3_2022 =", hasil)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai: ")
print("Objek1_2022 is objek3_2022=", objek1_2022 is objek3_2022)
print("Objek1_2022 == objek3_2022=", objek1_2022 == objek3_2022)