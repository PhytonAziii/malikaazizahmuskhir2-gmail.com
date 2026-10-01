# Program perulangan for untuk membuat segitiga

tinggi_2022 = int(input("Masukkan tinggi segitiga:"))

for i_2022 in range(1, tinggi_2022 + 1):
    for j_2022 in range(1, tinggi_2022 - i_2022 + 1):
        print(" ", end=" ")
    for k_2022 in range(1, 2 * i_2022):
        print("*", end=" ")
    print()