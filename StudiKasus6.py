import json

FILE_JSON = "Data.json"

def muat_data():
    if open(FILE_JSON, "a").close() == None:
        with open(FILE_JSON, "r", encoding="utf-8") as f:
            isi = f.read().strip()
            if isi:
                data = json.loads(isi)
                return data
            return []

def simpan_data(data):
    with open(FILE_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def tampilkan_data(data):
    print("\n" + "="*45)
    print("         HISTORI NILAI MAHASISWA")
    print("="*45)
    
    if not data:
        print("Belum ada data nilai tersimpan.")
    else:
        print("NIM | Nama | Nilai")
        print("-" * 45)
        for mhs in data:
            print(f"{mhs['nim']} | {mhs['nama']} | {mhs['nilai']}")
    print("="*45 + "\n")

def tambah_data(data):
    print("\n--- Tambah Data Nilai Baru ---")
    nim = input("Masukkan NIM   : ").strip()
    nama = input("Masukkan Nama  : ").strip()
    
    while True:
        input_nilai = input("Masukkan Nilai : ").strip()
        
        if input_nilai.replace('.', '', 1).isnumeric():
            nilai = float(input_nilai)
            if 0 <= nilai <= 100:
                break
            print("Nilai harus berada di rentang 0 - 100.")
        else:
            print("Input tidak valid. Harap masukkan angka.")

    mahasiswa_baru = {
        "nim": nim,
        "nama": nama,
        "nilai": nilai
    }
    
    data.append(mahasiswa_baru)
    simpan_data(data)
    print(f"Data nilai untuk {nama} berhasil ditambahkan dan disimpan!")

def main():
    data_nilai = muat_data()
    
    while True:
        print("\n=== SISTEM PENCATATAN NILAI MAHASISWA ===")
        print("1. Tampilkan Seluruh Data Nilai")
        print("2. Tambah Data Nilai Baru")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ").strip()
        
        if pilihan == "1":
            tampilkan_data(data_nilai)
        elif pilihan == "2":
            tambah_data(data_nilai)
        elif pilihan == "3":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1, 2, atau 3.")

if __name__ == "__main__":
    main()