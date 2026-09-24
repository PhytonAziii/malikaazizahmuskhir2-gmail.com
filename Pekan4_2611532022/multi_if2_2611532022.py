# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakn fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_2022 = float(input("Masukkan total belanja (Rp): "))

# Input satus member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2022 = input("Apakah Anda Member? (y/t): ").strip().lower()
is_member_2022 = input_member_2022 in ["y", "ya"]
# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2022 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2022 = input_promo_2022 in ["y", "ya"]

total_diskon_persen_2022 = 0

#multi-if terpisah: setiap kondisi diperiksa secara indepeenden
# Diskon bisa ditumpuk (akumulasi) jika memenuhi bebrapa syarat sekaligus

if total_belanja_2022 > 1000000:
    total_diskon_persen_2022 += 10 #Diskon Belanja Besar

if is_member_2022:
    total_diskon_persen_2022 += 5 #Diskon Member

if kode_promo_valid_2022:
    total_diskon_persen_2022 += 15 #Doskon Vocher

#menghitung nominal diskon dan total bayar
nominal_diskon_2022 = total_belanja_2022 * (total_diskon_persen_2022/ 100)
total_bayar_2022 = total_belanja_2022 - nominal_diskon_2022

#output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_2022}% (rp {nominal_diskon_2022:,.0f})")
print(f"Total Bayar : Rp {total_bayar_2022:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_2022}%")
# output total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid