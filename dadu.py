import random

def lempar_dadu_20(jumlah_lemparan):
    hasil = [0] * 20  # List untuk menyimpan frekuensi kemunculan angka 1-20
    
    # Simulasi lemparan dadu
    for i in range(jumlah_lemparan):
        angka = random.randint(1, 20)
        hasil[angka - 1] += 1  # Menambah frekuensi untuk angka yang muncul

    print(f"Jumlah lemparan: {jumlah_lemparan}")
    
    # Menampilkan jumlah kemunculan dan peluang tiap angka
    for angka in range(1, 21):
        frekuensi = hasil[angka - 1]
        peluang = frekuensi / jumlah_lemparan
        print(f"Angka {angka} muncul: {frekuensi} kali, Peluang: {peluang:.2f}")
    
    # Probabilitas teoretis
    probabilitas_teoretis = 1 / 20
    print(f"\nProbabilitas teoretis setiap angka pada dadu 20 sisi: {probabilitas_teoretis:.2f}")

# Meminta input jumlah lemparan
jumlah_lemparan = int(input("Masukkan jumlah lemparan: "))
lempar_dadu_20(jumlah_lemparan)
