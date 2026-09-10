# Buat file dengan nama Boolean_2611532022.py
#nama variable ditambah 4 digit nim terakhir contoh: nama_1234
# Deklarasi variable dengan tipe data boolean
is_lulus_2022 = True
is_cumlaude_2022 = True

# Menggunakan Boolean
nilai_2022 = 85
batas_lulus_2022 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_2022 = nilai_2022 >= batas_lulus_2022 #Hasilnya akan True

print("=== Check Kelulusan === ")
print("Nilai:", nilai_2022)
print("Apakah lulus?:", status_kelulusan_2022)
if is_lulus_2022 and is_cumlaude_2022:
    print("Selamat, Anda lulus dengan prediket cumlaude!")
    