# Studi_Kasus_6_Muhammad-Omar-Zahraan_2609116023

**Nama: Muhammad Omar Zahraan**

**NIM: 2609116023**

**Kelas: A**

**Penjelasan Kode Program**

<img width="385" height="137" alt="image" src="https://github.com/user-attachments/assets/8fe8710c-555e-4833-baf2-08979622e5c6" />
<br>

Di awal, kode ini melakukan import modul bawaan json untuk urusan serialisasi data. Dibuat juga variabel global FILE_JSON = "Data.json" sebagai path file database lokalnya. Variabel ini diset di atas supaya kalau mau ganti nama file database, tidak perlu edit satu-satu di dalam fungsi.

<img width="672" height="187" alt="image" src="https://github.com/user-attachments/assets/56eafc53-d81b-4d11-8934-51126cbcec58" />
<br>

Fungsi ini bertugas sebagai loader data awal dari file Data.json ke dalam memory (RAM). Karena tidak pakai block try-except, digunakan trick open(FILE_JSON, "a").close() agar sistem otomatis membuat filenya dulu kalau filenya belum ada. Setelah itu, file dibaca, di-parse dari string JSON menjadi bentuk list of dictionaries pakai json.loads(), lalu di-return. Jika filenya kosong, fungsi langsung mengembalikan array / list kosong [].

<img width="607" height="72" alt="image" src="https://github.com/user-attachments/assets/75b9f6f2-923b-4b5d-8c4d-dc549b1006da" />
<br>

Fungsi ini adalah logika persistence untuk menyimpan perubahan array ke storage lokal. Fungsi ini membuka file Data.json dengan mode write ("w"), lalu menimpa isinya menggunakan json.dump(). Opsi indent=4 dipakai supaya output file JSON tetap rapi dan terstruktur (pretty-printed).

<img width="752" height="312" alt="image" src="https://github.com/user-attachments/assets/7c0893f8-f60e-438f-926a-e0689994418f" />
<br>

Fungsi ini bertindak sebagai layer view untuk menampilkan data di terminal. Pertama, fungsi mengecek kondisi array (if not data); kalau masih kosong, langsung dimunculkan log bahwa data belum ada. Kalau array berisi, program melakukan looping for untuk melakukan render kolom NIM, Nama, dan Nilai per baris.

<img width="685" height="506" alt="image" src="https://github.com/user-attachments/assets/c7bc4078-28dc-4812-9c94-5760390ba048" />
<br>

Fungsi ini menangani proses input atau penambahan data baru. Setelah mengambil string NIM dan Nama, ada validasi input nilai di dalam looping while True. Pengecekan berbasis input_nilai.replace('.', '', 1).isnumeric() dipakai menggantikan try-except untuk memastikan user menginput type-data float/integer yang valid di rentang 0-100. Setelah lolos validasi, data di-push ke array dengan .append(), lalu fungsi simpan_data() dipanggil agar ter-sync ke file .json.

<img width="820" height="552" alt="image" src="https://github.com/user-attachments/assets/77ef1ef2-1d48-491f-bc15-47803d2541fe" />
<br>

Fungsi main() adalah core controller yang menjalankan infinite loop while True untuk menangani navigasi CLI menu. Pengguna bisa memilih route menu untuk read, create, atau exit. Blok if __name__ == "__main__": di baris akhir berfungsi sebagai entry point utama agar fungsi main() otomatis di-run ketika file Python ini dipanggil via terminal.

**Output program**

<img width="887" height="735" alt="image" src="https://github.com/user-attachments/assets/e451f640-1145-4ad7-92f1-13d6e35184a6" />
<br>

**Bukti Data Tersimpan**
<img width="1385" height="747" alt="Screenshot 2026-10-07 201647" src="https://github.com/user-attachments/assets/e8b9d43c-a7fd-42d0-8711-f7b7a8d365ac" />

