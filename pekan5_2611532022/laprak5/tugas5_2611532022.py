# Program Jam Pasir Kristal Palindromik Berbingkai

n_2022 = int(input("Masukkan ukuran skala jam pasir (N): "))

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
print()

# Bingkai atas
print("#", end="")
for j_2022 in range(1, 4 * n_2022 + 6):
    print("=", end="")
print("#")

# Fase 1: Jam pasir atas
for baris_2022 in range(n_2022, 0, -1):

    print("| ", end="")

    # Spasi kiri
    for spasi_2022 in range(1, n_2022 - baris_2022 + 1):
        print(" ", end=" ")

    # Angka menurun
    for angka_2022 in range(baris_2022, 0, -1):
        print(angka_2022, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2022 in range(1, baris_2022 + 1):
        print(" ", end="")
        print(angka_2022, end="")

    # Spasi kanan
    for spasi_2022 in range(1, n_2022 - baris_2022 + 1):
        print(" ", end=" ")

    print(" |")

# Fase 2: Titik pusat
print("| ", end="")

for spasi_2022 in range(1, n_2022 + 1):
    print(" ", end=" ")

print("<*>", end="")

for spasi_2022 in range(1, n_2022 + 1):
    print(" ", end=" ")

print(" |")

# Fase 3: Jam pasir bawah
for baris_2022 in range(1, n_2022 + 1):

    print("| ", end="")

    # Spasi kiri
    for spasi_2022 in range(1, n_2022 - baris_2022 + 1):
        print(" ", end=" ")

    # Angka menurun
    for angka_2022 in range(baris_2022, 0, -1):
        print(angka_2022, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2022 in range(1, baris_2022 + 1):
        print(" ", end="")
        print(angka_2022, end="")

    # Spasi kanan
    for spasi_2022 in range(1, n_2022 - baris_2022 + 1):
        print(" ", end=" ")

    print(" |")

# Bingkai bawah
print("#", end="")
for j_2022 in range(1, 4 * n_2022 + 6):
    print("=", end="")
print("#")