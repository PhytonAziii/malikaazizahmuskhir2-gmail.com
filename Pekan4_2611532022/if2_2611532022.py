# Buat file dengan nama if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakn fungsi input()

ipk_2022 = float(input("Input IPK Anda = "))

if ipk_2022 > 2.75:
    print("Anda Lluas Sangat Memuaskan dengan IPK " + str(ipk_2022))
else: 
    print("Anda Tidak Lulus")
print("Program Selesai")