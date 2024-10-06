import random

def lempar_koin(jumlah_lemparan):
    angka = 0
    gambar = 0
    
    for i in range(jumlah_lemparan):
        hasil = random.choice(["angka", "gambar"])
        if hasil == "angka":
            angka += 1
        else:
            gambar += 1

    peluang_angka = angka / jumlah_lemparan
    peluang_gambar = gambar / jumlah_lemparan

    # Probabilitas teoretis untuk koin adil
    probabilitas_teoretis_angka = 0.5
    probabilitas_teoretis_gambar = 0.5

    print(f"Jumlah lemparan: {jumlah_lemparan}")
    print(f"Angka muncul: {angka} kali")
    print(f"Gambar muncul: {gambar} kali")
    print(f"Peluang angka dari simulasi: {peluang_angka:.2f}")
    print(f"Peluang gambar dari simulasi: {peluang_gambar:.2f}")
    print(f"Probabilitas teoretis angka: {probabilitas_teoretis_angka}")
    print(f"Probabilitas teoretis gambar: {probabilitas_teoretis_gambar}")

# Meminta input jumlah lemparan
jumlah_lemparan = int(input("Masukkan jumlah lemparan: "))
lempar_koin(jumlah_lemparan)
