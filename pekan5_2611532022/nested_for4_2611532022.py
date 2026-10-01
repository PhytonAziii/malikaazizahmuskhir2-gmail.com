# Buat nama file dengan nama nested_for4_2611532022.py
# Buat program utuk perulangan for dalam phyton
# Nama variabel ditambah 4 digit nim terakhir contoh:1234
# Program ini menggunakn fungsi input()

tinggi_2022 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2022 % 2 != 0:
    print("Tinggi harus genap!")
else:
    a_2022 = tinggi_2022
    c_2022 = a_2022
    lebar_2022 = (2 * tinggi_2022) - 2

    for i_2022 in range (1, tinggi_2022 + 1):
        b_2022 = c_2022 + 1

        for j_2022 in range(1, lebar_2022 + 1):

            # Baris atas dan bawah
            if i_2022 == 1 or i_2022 == tinggi_2022:
               if j_2022 == 1 or j_2022 == lebar_2022:
                   print("#", end="")
               else:
                   print("=", end="")

            # Baris isi
            else:
                if j_2022 == 1 or j_2022 == lebar_2022:
                    print("|", end="")
                else:
                    if j_2022 == c_2022:
                        print("<", end="")
                    elif j_2022 == b_2022:
                        print(">", end="")
                    elif j_2022 == (lebar_2022 - c_2022 ):
                        print("<", end="")
                    elif j_2022 == (lebar_2022 - c_2022 + 1):
                        print(">", end="")
                    elif j_2022 > b_2022 and j_2022 < (lebar_2022 - c_2022):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli java
        a_2022 -= 2

        if a_2022 <= 0:
            c_2022 = (-a_2022) + 2
        else:
            c_2022 = a_2022