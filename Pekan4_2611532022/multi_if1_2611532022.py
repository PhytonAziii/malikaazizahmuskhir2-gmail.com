# Buat file dengan nama multi_if1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakn fungsi input()

umur_2022 = int(input("Input Umur Anda"))
sim_2022 = input("Apakah Anda Sudah Punya SIM C (y/t): ")

if umur_2022 >= 17 and sim_2022 == 'y':
    print("Anda Suddah Dewasa dan Boleh Bawa Motor")

if umur_2022 >= 17 and sim_2022 != 'y':
    print("Anda Suddah Dewasa tetapi Tidak Boleh Bawa Motor")

if umur_2022 < 17 and sim_2022 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_2022 < 17 and sim_2022 != 'y':
    print("Anda Belum Cukup Umur untuk Bawa Motor")
