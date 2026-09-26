# Buat file dengan nama studi_kasus_2611532022.py
# Program Sistem Loket Alpro Adventure Park
# Nama variabel ditambah 4 digit NIM terakhir

import sys

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# Input Data Pengunjung
nama_2022 = input("Masukkan Nama Pengunjung        : ")
umur_2022 = int(input("Input umur anda                 : "))

sim_2022 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()

jumlah_tiket_2022 = int(input("Masukkan jumlah tiket           : "))

# Validasi jumlah tiket menggunakan if tunggal
if jumlah_tiket_2022 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

# Pilihan Paket Wahana
print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba         (Rp 50,000)")
print("2. Arung Jeram          (Rp 75,000)")
print("3. Motor ATV Ekstrim    (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP       (Rp 220,000)")

paket_2022 = int(input("Masukkan nomor paket (1-5) : "))

# Pemilihan wahana menggunakan match-case
match paket_2022:
    case 1:
        nama_wahana_2022 = "Wahana Safari Rimba"
        harga_satuan_2022 = 50000

    case 2:
        nama_wahana_2022 = "Wahana Arung Jeram"
        harga_satuan_2022 = 75000

    case 3:
        nama_wahana_2022 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2022 = 120000

    case 4:
        nama_wahana_2022 = "Wahana Roller Coaster Kilat"
        harga_satuan_2022 = 100000

    case 5:
        nama_wahana_2022 = "Wahana All-Access VIP"
        harga_satuan_2022 = 220000

    case _:
        print("Paket wahana tidak valid!")
        sys.exit()

# Validasi jumlah tiket
if jumlah_tiket_2022 <= 0:
    print("Transaksi dihentikan karena jumlah tiket tidak valid.")
    sys.exit()

# Validasi izin kendali wahana
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_2022 == 3:
    if umur_2022 >= 17 and sim_2022 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")

    elif umur_2022 >= 17 and sim_2022 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")

    elif umur_2022 < 17 and sim_2022 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")

    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")

else:
    if umur_2022 >= 10:
        print("Status Akses: Anda memenuhi syarat umur untuk wahana.")
    else:
        print("Status Akses: Anda belum cukup umur untuk wahana ini.")

# Menghitung subtotal
subtotal_2022 = harga_satuan_2022 * jumlah_tiket_2022

# Input Member dan Promo
input_member_2022 = input("Apakah Anda member? (y/t)       : ").strip().lower()
input_promo_2022 = input("Apakah kode promo valid? (y/t) : ").strip().lower()

# Total diskon awal
total_diskon_persen_2022 = 0

# Multi-if untuk diskon akumulasi
if subtotal_2022 >= 200000:
    total_diskon_persen_2022 += 10

if input_member_2022 in ['y', 'ya']:
    total_diskon_persen_2022 += 5

if input_promo_2022 in ['y', 'ya']:
    total_diskon_persen_2022 += 15

if jumlah_tiket_2022 >= 5:
    total_diskon_persen_2022 += 5

# Menghitung nominal diskon dan total bayar
nominal_diskon_2022 = subtotal_2022 * (total_diskon_persen_2022 / 100)
total_bayar_2022 = subtotal_2022 - nominal_diskon_2022

# Audit total pembayaran
if total_bayar_2022 > 300000:
    catatan_layanan_2022 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_2022 = "Terima kasih telah berkunjung."

# Output
print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Nama Pengunjung : {nama_2022}")
print(f"Wahana         : {nama_wahana_2022}")
print(f"Harga Satuan   : Rp {harga_satuan_2022:,.0f}")
print(f"Jumlah Tiket   : {jumlah_tiket_2022}")
print(f"Subtotal Belanja : Rp {subtotal_2022:,.0f}")
print(f"Total Diskon   : {total_diskon_persen_2022}% (Rp {nominal_diskon_2022:,.0f})")
print(f"Total Bayar    : Rp {total_bayar_2022:,.0f}")
print(f"Catatan Layanan: {catatan_layanan_2022}")

print("\nProgram Selesai")