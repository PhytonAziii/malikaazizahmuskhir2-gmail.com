# Buat nama file dengan nama nested_for3_2611532022.py
# Buat program utuk perulangan for dalam phyton
# Nama variabel ditambah 4 digit nim terakhir contoh:1234
# Program ini menggunakn fungsi input()

batas_2022= int(input("Masukkan nilai batas :"))
for i_2022 in range(batas_2022 + 1):
    for j_2022 in range (batas_2022+1):
        print(i_2022+j_2022, end=" ")
    print() # pindah ke baris berikutnya