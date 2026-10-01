# Buat nama file dengan nama jumlah_genap_2611532022.py
# Buat program utuk perulangan for dalam phyton
# Nama variabel ditambah 4 digit nim terakhir contoh:1234
# Program ini menggunakn fungsi input()

ulang_2022 = int(input("masukkan nilai batas ;"))

jumlah_genap_2022 = 0
for i_2022 in range(1, ulang_2022 + 1):
    if i_2022 % 2 == 0:
        print(i_2022, end=" ")
        jumlah_genap_2022 = jumlah_genap_2022 + i_2022

        if i_2022 < jumlah_genap_2022:
            print("+", end ="")
        else:
            print("=", jumlah_genap_2022)
print()
print("Jumlah genap = ", jumlah_genap_2022)