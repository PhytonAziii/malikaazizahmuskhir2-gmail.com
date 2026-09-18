# Buat file dengan nama Tugas3_2611532022.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Program operator Sistem Simulasi Transaksi dan Validasi Akses Toko

# 1. INPUT DATA PELANGGAN
nama_2022 = input("Masukkan nama pelanggan: ")
status_2022 = input("Masukkan status (member/nonmember): ")
jumlah_2022 = int(input("Masukkan jumlah barang: "))
harga_2022 = int(input("Masukkan harga satu barang: "))
promo_2022 = input("Masukkan kode promo (HEMAT10/HEMAT20/GRATISONGKIR): ")

# 2. OPERASI ARITMATIKA
belanja_2022 = jumlah_2022 * harga_2022

# Menghitung rata-rata harga per barang
rata_rata_2022 = belanja_2022
if jumlah_2022 > 0:
    rata_rata_2022 /= jumlah_2022

# 3. OPERASI PERBANDINGAN
member_2022 = status_2022 == "member"
belanja_cukup_2022 = belanja_2022 >= 100000
barang_cukup_2022 = jumlah_2022 >= 3
promo_valid_2022 = promo_2022 in ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# 4. OPERASI LOGIKA
akses_promo_2022 = (
    member_2022
    and belanja_cukup_2022
    and barang_cukup_2022
    and promo_valid_2022
)

akses_toko_2022 = (
    status_2022 == "member"
    or status_2022 == "nonmember"
)

# 5. OPERASI KEANGGOTAAN
daftar_promo_2022 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
promo_tersedia_2022 = promo_2022 in daftar_promo_2022
promo_tidak_tersedia_2022 = promo_2022 not in daftar_promo_2022

# 6. OPERASI IDENTITAS
daftar_promo_2_2022 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
daftar_promo_3_2022 = daftar_promo_2022

identitas_sama_2022 = daftar_promo_2_2022 is daftar_promo_3_2022
identitas_berbeda_2022 = daftar_promo_2_2022 is not daftar_promo_3_2022
isi_sama_2022 = daftar_promo_2_2022 == daftar_promo_3_2022

# 7. OPERASI PENUGASAN
poin_2022 = 0
poin_2022 += jumlah_2022
poin_2022 *= 2

# 8. MENGHITUNG DISKON
diskon_2022 = 0

if akses_promo_2022:
    if promo_2022 == "HEMAT20":
        diskon_2022 = belanja_2022 * 20 // 100
    elif promo_2022 == "HEMAT10":
        diskon_2022 = belanja_2022 * 10 // 100

# Mengurangi total belanja dengan diskon
total_bayar_2022 = belanja_2022
total_bayar_2022 -= diskon_2022

# 9. OPERASI BITWISE
status_bit_2022 = 0

if member_2022:
    status_bit_2022 |= 1

if belanja_cukup_2022:
    status_bit_2022 |= 2

if barang_cukup_2022:
    status_bit_2022 |= 4

if promo_valid_2022:
    status_bit_2022 |= 8

bit_and_2022 = status_bit_2022 & 1
bit_or_2022 = status_bit_2022 | 2
bit_xor_2022 = status_bit_2022 ^ 4

# 10. MENAMPILKAN HASIL
print("\n===== HASIL TRANSAKSI =====")
print("Nama pelanggan:", nama_2022)
print("Status pelanggan:", status_2022)
print("Jumlah barang:", jumlah_2022)
print("Harga satu barang:", harga_2022)
print("Total belanja:", belanja_2022)
print("Rata-rata harga barang:", rata_rata_2022)

print("\n===== VALIDASI =====")
print("Pelanggan adalah member:", member_2022)
print("Belanja minimal Rp100.000:", belanja_cukup_2022)
print("Jumlah barang minimal 3:", barang_cukup_2022)
print("Kode promo valid:", promo_valid_2022)
print("Akses toko:", akses_toko_2022)
print("Akses promo:", akses_promo_2022)

print("\n===== HASIL PEMBAYARAN =====")
print("Diskon:", diskon_2022)
print("Total pembayaran:", total_bayar_2022)
print("Poin pelanggan:", poin_2022)

print("\n===== OPERASI KEANGGOTAAN =====")
print("Promo tersedia:", promo_tersedia_2022)
print("Promo tidak tersedia:", promo_tidak_tersedia_2022)

print("\n===== OPERASI IDENTITAS =====")
print("Objek 2 dan 3 sama:", identitas_sama_2022)
print("Objek 2 dan 3 berbeda:", identitas_berbeda_2022)
print("Isi daftar sama:", isi_sama_2022)

print("\n===== OPERASI BITWISE =====")
print("Status bit:", status_bit_2022)
print("Bitwise AND:", bit_and_2022)
print("Bitwise OR:", bit_or_2022)
print("Bitwise XOR:", bit_xor_2022)