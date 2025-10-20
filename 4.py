JADWAL_KULIAH = [
    {"hari": "senin", "matakuliah": "Kalkulus", "jam": "08:00 - 10:00", "ruang": "D.3.1"},
    {"hari": "selasa", "matakuliah": "Struktur Data", "jam": "10:00 - 12:00", "ruang": "D.3.2"},
    {"hari": "rabu", "matakuliah": "Pemrograman Python", "jam": "13:00 - 15:00", "ruang": "Lab 1"},
    {"hari": "senin", "matakuliah": "Basis Data", "jam": "13:00 - 15:00", "ruang": "D.3.1"},
    {"hari": "rabu", "matakuliah": "Kecerdasan Buatan", "jam": "08:00 - 10:00", "ruang": "D.3.2"},
    {"hari": "kamis", "matakuliah": "Jaringan Komputer", "jam": "10:00 - 12:00", "ruang": "Lab 2"},
    {"hari": "jumat", "matakuliah": "Sistem Operasi", "jam": "08:00 - 10:00", "ruang": "D.3.3"},
    {"hari": "kamis", "matakuliah": "Grafika Komputer", "jam": "13:00 - 15:00", "ruang": "Lab 1"},
]

def jadwal_hari(hari):
    """
    Mencari dan menampilkan semua jadwal untuk hari tertentu.
    Fungsi ini adalah inti dari logika pencarian.
    """
    hari_dicari = hari.lower().strip() 
    jadwal_ditemukan = []

    for jadwal in JADWAL_KULIAH:
        if jadwal["hari"] == hari_dicari:
            jadwal_ditemukan.append(jadwal)
    
    if not jadwal_ditemukan:
        print(f"\nTidak ada jadwal untuk hari {hari.title()}.")
    else:
        print(f"\n--- Jadwal Hari {hari.title()} ---")
        for jadwal in jadwal_ditemukan:
            print(f"- Matakuliah: {jadwal['matakuliah']} | Jam: {jadwal['jam']} | Ruang: {jadwal['ruang']}")

def main():
    """Fungsi utama untuk menjalankan program secara interaktif."""
    print("=== Sistem Informasi Jadwal Kuliah ===")
    
    hari_input = input("Masukkan nama hari untuk melihat jadwal (misal: Senin): ")
    
    jadwal_hari(hari_input)

    print("\n" + "="*40 + "\n")

    print("Penjelasan: Fungsi ini bekerja dengan cara melakukan iterasi untuk mengecek satu per satu setiap elemen dictionary di dalam list jadwal.")



if __name__ == "__main__":
    main()