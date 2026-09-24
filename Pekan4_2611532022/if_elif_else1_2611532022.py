# Buat file dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakn fungsi input()

umur_2022 = int(input("Input Umur Anda"))
sim_2022 = input("Apakah Anda Sudah Punya SIM C: ")[0]

if umur_2022 >= 17 and sim_2022 == 'y':
    print("Anda Suddah Dewasa dan Boleh Bawa Motor")
elif umur_2022 >= 17 and sim_2022 != 'y':
    print("Anda Suddah Dewasa tetapi Tidak Boleh Bawa Motor")
elif umur_2022 < 17 and sim_2022 == 'y':
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan Tidak Boleh Bawa Motor")
print("Program Selesai")