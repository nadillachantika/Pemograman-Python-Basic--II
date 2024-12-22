import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showinfo
from tkinter import PhotoImage

window = tk.Tk()
# ubah background
window.configure(bg="white")
# adjust size
window.geometry("500x500")
# ubah title
window.title("Program Sapa")

input_frame = ttk.Frame(window)
input_frame.pack(pady=20, padx=20, fill="x", expand=True)

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar() 
SUHU_CELCIUS = tk.DoubleVar()

# Konversi ComboBox harus dideklarasikan terlebih dahulu


def tombol_sapa():
    if not NAMA_DEPAN.get().strip():
        showinfo(title="Error", message="Nama Depan Tidak Boleh Kosong")
    else:
        tipe_konversi = konversi_combo.get()
        celcius = SUHU_CELCIUS.get()
        
        # Lakukan konversi suhu berdasarkan pilihan
        if tipe_konversi == "Fahrenheit":
            suhu_hasil = (celcius * 9/5) + 32
            hasil_suhu = f"{suhu_hasil:.2f}°F"
        elif tipe_konversi == "Kelvin":
            suhu_hasil = celcius + 273.15
            hasil_suhu = f"{suhu_hasil:.2f}K"
        else:
            hasil_suhu = f"{celcius}°C"  # Default Celcius

        # Buat pesan dengan nama dan suhu yang sudah dikonversi
        pesan = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}!\nSuhu yang anda masukkan adalah {hasil_suhu}"
        showinfo(title="Pesan", message=pesan)


# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
nama_depan_label.pack(padx=10, pady=10, fill="x", expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang")
nama_belakang_label.pack(padx=10, pady=10, fill="x", expand=True)

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Label untuk input suhu celcius
suhu_label = ttk.Label(input_frame, text="Suhu (Celcius):")
suhu_label.pack(padx=10, pady=10, fill="x", expand=True)

konversi_combo = ttk.Combobox(input_frame, values=["Celcius", "Fahrenheit", "Kelvin"])
konversi_combo.pack(pady=20, padx=20, fill="x", expand=True)
konversi_combo.set("Celcius")  # Default ke Celcius

# 6. Entry suhu Celcius
suhu_entry = ttk.Entry(input_frame, textvariable=SUHU_CELCIUS)
suhu_entry.pack(padx=10, fill="x", expand=True)

# 7. Tombol Sapa!
tombol_sapa = ttk.Button(input_frame, text="Sapa!", command=tombol_sapa)
tombol_sapa.pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()


def tugas_3(nama, usia, pekerjaan):
    print(f"Hello {nama}, usia anda {usia}, pekerjaan anda {pekerjaan}")
    