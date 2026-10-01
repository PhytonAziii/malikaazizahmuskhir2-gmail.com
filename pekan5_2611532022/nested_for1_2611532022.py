# Buat nama file dengan nama nested_for1_2611532022.py
# Buat program utuk perulangan for dalam phyton
# Nama variabel ditambah 4 digit nim terakhir contoh:1234
# Program ini menggunakn fungsi input()

batas2022 = int(input("Masukkan nilai batas ;"))
for line in range(1, batas2022 + 1):
    for j_2022 in range(1, line + 1):
        print(j_2022, end=" ")
    print(line)