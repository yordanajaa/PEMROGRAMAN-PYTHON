try:
    # Menggunakan int() untuk menerima input bilangan bulat
    setoran1 = int(input("Masukkan setoran pertama: "))
    setoran2 = int(input("Masukkan setoran kedua: "))
    setoran3 = int(input("Masukkan setoran ketiga: "))

    if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
        print("Input tidak valid.")
    else:
        total_setoran = setoran1 + setoran2 + setoran3
        print(f"Total setoran Anda: Rp {total_setoran:,}") 

        if total_setoran >= 600000:
            print("Kategori: Tinggi")
        elif total_setoran >= 300000:
            print("Kategori: Sedang")
        else:
            print("Kategori: Rendah")

except ValueError:
   
    print("Input tidak valid, harap masukkan angka bilangan bulat (tanpa koma).")