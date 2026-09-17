# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1008
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_2022 = int(input("Masukkan angka bitwise-1: "))
angka2_2022 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_2022,"| biner =",bin(angka1_2022))
print("angka1 =",angka2_2022,"| biner =",bin(angka2_2022))

# Bitwise AND
hasil_2022 = angka1_2022 & angka2_2022
print("\nBitwise AND (&)")
print(angka1_2022,"&",angka2_2022,hasil_2022)
print("Biner hasil =",bin(hasil_2022))
print("Biner hasil (8 bit) =",format(hasil_2022,"08b"))

# Bitwise OR
hasil_2022 = angka1_2022 | angka2_2022
print("\nBitwise OR (|)")
print(angka1_2022,"|",angka2_2022,hasil_2022)
print("Biner hasil =",bin(hasil_2022))
print("Biner hasil (8 bit) =",format(hasil_2022,"08b"))

# Bitwise XOR
hasil_2022 = angka1_2022 ^ angka2_2022
print("\nBitwise XOR (^)")
print(angka1_2022,"^",angka2_2022,hasil_2022)
print("Biner hasil =",bin(hasil_2022))
print("Biner hasil (8 bit) =",format(hasil_2022,"08b"))

# Bitwise NOT
hasil_2022 = ~angka1_2022
print("\nBitwise NOT (~)")
print(angka1_2022,"~",angka2_2022,hasil_2022)
print("Biner hasil =",bin(hasil_2022))
print("Biner hasil (8 bit) =",format(hasil_2022,"08b"))

# Bitwise geser kiri
jumlah_geser_2022 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2022 = angka1_2022 << jumlah_geser_2022
print("\nBitwise geser kiri (<<)")
print(angka1_2022,"<<",jumlah_geser_2022,"=",hasil_2022)
print("Biner hasil =",bin(hasil_2022))
print("Biner hasil (8 bit) =",format(hasil_2022,"08b"))

# Bitwise geser kanan
hasil_2022= angka1_2022 >> jumlah_geser_2022
print("\nBitwise geser kanan (>>)")
print(angka1_2022,">>",jumlah_geser_2022,"=",hasil_2022)
print("Biner hasil =",bin(hasil_2022))
print("Biner hasil (8 bit) =",format(hasil_2022,"08b"))