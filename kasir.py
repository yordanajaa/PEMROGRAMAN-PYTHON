import requests
import datetime

MENU = {
    "kopi": 15000,
    "teh": 12000,
    "roti": 10000,
    "jus": 20000,
}

PROMO_API_URL = "https://api.quotable.io/random?tags=technology,famous-quotes"

def dapatkan_promo_harian():
    try:
        response = requests.get(PROMO_API_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"Promo Hari Ini: '{data['content']}' - {data['author']}"
        else:
            return "Tidak bisa mengambil promo saat ini. Selamat berbelanja!"
    except requests.exceptions.RequestException:
        return "Gagal terhubung ke server promo. Cek koneksi internet Anda."

def tampilkan_menu():
    print("\n--- MENU KASIR KODE ---")
    for item, harga in MENU.items():
        print(f"- {item.title():<10}: Rp {harga:,.0f}")
    print("-------------------------")

def jalankan_kasir():
    print(dapatkan_promo_harian())
    
    keranjang = {}
    total_harga = 0

    while True:
        tampilkan_menu()
        
        pesanan = input("Masukkan menu yang dipesan (ketik 'bayar' untuk selesai): ").lower()

        if pesanan == 'bayar':
            if not keranjang:
                print("Anda belum memesan apapun. Terima kasih.")
                break
            else:
                break

        if pesanan not in MENU:
            print(f"Maaf, menu '{pesanan}' tidak tersedia. Silakan coba lagi.")
            continue

        try:
            jumlah = int(input(f"Jumlah '{pesanan.title()}' : "))
            if jumlah <= 0:
                print("Jumlah pesanan harus lebih dari nol.")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk jumlah.")
            continue

        harga_satuan = MENU[pesanan]
        subtotal = harga_satuan * jumlah
        total_harga += subtotal
        
        keranjang[pesanan] = keranjang.get(pesanan, 0) + jumlah
        print(f"-> {jumlah}x {pesanan.title()} ditambahkan ke keranjang.")

    if keranjang:
        print("\n--- STRUK PEMBAYARAN ---")
        waktu_transaksi = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"Waktu: {waktu_transaksi}")
        print("--------------------------")
        for item, jumlah in keranjang.items():
            subtotal_item = MENU[item] * jumlah
            print(f"{jumlah}x {item.title():<10} | Rp {subtotal_item:,.0f}")
        print("--------------------------")
        print(f"TOTAL      : Rp {total_harga:,.0f}")
        print("==========================")
        print("Terima kasih telah berbelanja!")

if __name__ == "__main__":
    jalankan_kasir()