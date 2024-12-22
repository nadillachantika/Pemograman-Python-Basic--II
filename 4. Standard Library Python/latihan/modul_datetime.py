from datetime import datetime as dt
import hashlib

sekarang = dt.now()
print(sekarang)

# input tanggal tujuan 
tanggal_tujuan = input("Masukkan tanggal tujuan (YYYY-MM-DD): ")
tanggal_tujuan_dt = dt.strptime(tanggal_tujuan, "%Y-%m-%d") # konversi ke format datetime

sisa_hari = (tanggal_tujuan_dt - sekarang).days


print(f"Sisa hari sampai tanggal {tanggal_tujuan} adalah {sisa_hari} hari")

