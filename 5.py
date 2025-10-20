import csv
import json
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("rekap.log"), 
        logging.StreamHandler()         
    ]
)

def rekap_kehadiran_uts():
    """
    Skrip untuk merekap kehadiran UTS, dari data mentah ke CSV,
    lalu diolah dan disimpan sebagai ringkasan JSON.
    """
    try:
        logging.info("Memulai proses rekap kehadiran UTS.")
        
        data_folder = Path("data")
        data_folder.mkdir(exist_ok=True)
        
        data_presensi = [
            {'nim': 'A11.2023.001', 'nama': 'yordan', 'hadir_uts': 1},
            {'nim': 'A11.2023.002', 'nama': 'Citra', 'hadir_uts': 0},
            {'nim': 'A11.2023.003', 'nama': 'Doni', 'hadir_uts': 1},
            {'nim': 'A11.2023.004', 'nama': 'tono', 'hadir_uts': 1},
            {'nim': 'A11.2023.005', 'nama': 'ciput', 'hadir_uts': 1},
            {'nim': 'A11.2023.006', 'nama': 'kiwi', 'hadir_uts': 1},
        ]
        file_csv = data_folder / "presensi.csv"

        with file_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data_presensi[0].keys())
            writer.writeheader()
            writer.writerows(data_presensi)
        logging.info(f"Berhasil menulis data presensi ke '{file_csv}'.")

        total_mahasiswa = 0
        jumlah_hadir = 0
        with file_csv.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data_dari_csv = list(reader)
            total_mahasiswa = len(data_dari_csv)
            for baris in data_dari_csv:
                if int(baris['hadir_uts']) == 1:
                    jumlah_hadir += 1
        
        persentase = (jumlah_hadir / total_mahasiswa * 100) if total_mahasiswa > 0 else 0
        
        ringkasan = {
            "total_mahasiswa": total_mahasiswa,
            "jumlah_hadir": jumlah_hadir,
            "persentase_kehadiran": f"{persentase:.2f}%"
        }
        
        file_json = data_folder / "ringkasan.json"

        with file_json.open("w", encoding="utf-8") as f:
            json.dump(ringkasan, f, indent=4)
        logging.info(f"Berhasil menyimpan ringkasan ke '{file_json}'.")

    except IOError as e:
        logging.error(f"Gagal melakukan operasi file: {e}")
    except Exception as e:
        logging.error(f"Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    rekap_kehadiran_uts()