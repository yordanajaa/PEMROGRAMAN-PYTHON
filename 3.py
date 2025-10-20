TARIF_DASAR_KOTA = {
    "jakarta": 10000,
    "bandung": 8000,
    "surabaya": 12000,
}

def hitung_ongkir(berat_kg, kota, asuransi=False):
    kota = kota.lower()
    
    if kota not in TARIF_DASAR_KOTA:
        return 


    tarif_dasar = TARIF_DASAR_KOTA[kota]
    biaya_berat = 2000 * berat_kg
    biaya_asuransi = 3000 if asuransi else 0
    
    total_ongkir = tarif_dasar + biaya_berat + biaya_asuransi
    return total_ongkir

# Contoh 1: Pengiriman 2.5 kg ke Jakarta tanpa asuransi
ongkir1 = hitung_ongkir(2.5, "Jakarta")
print(f"Ongkir ke Jakarta (2.5 kg, tanpa asuransi): Rp {ongkir1:,.0f}")

# Contoh 2: Pengiriman 5 kg ke Surabaya dengan asuransi
ongkir2 = hitung_ongkir(5, "Surabaya", asuransi=True)
print(f"Ongkir ke Surabaya (5 kg, dengan asuransi): Rp {ongkir2:,.0f}")