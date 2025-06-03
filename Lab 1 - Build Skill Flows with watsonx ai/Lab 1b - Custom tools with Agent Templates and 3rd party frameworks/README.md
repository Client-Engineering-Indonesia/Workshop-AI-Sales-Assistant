# Membuat AI Agent dengan **watsonx.ai** & **Crew AI**

Pada lab ini, kita akan membuat **Sales Analyzer Agent** dengan memanfaatkan *watsonx.AI Agent Lab* dan framework **Crew AI**. Agent ini akan menganalisis data penjualan sebuah produk untuk membantu proses procurement.

> **Catatan** File‐file yang diperlukan dapat diunduh dari folder “📂 *to‑be‑provided*”.

---

## Tahapan Pembuatan Agent

### Step 1 — Membuat *Project*
1. Jika ini pertama kali Anda menggunakan akun ini, buatlah **Project** baru sebelum membuka Agent Lab. 
2. Jika sudah punya, Anda boleh memakai project yang ada.

![Project](https://github.com/user-attachments/assets/1282049d-f55e-47f6-9ff9-e176dd3e4af8)

---

### Step 2 — Mengasosiasikan watsonx.ai Runtime
1. Buka **Manage → Services & Integrations → Associate Service**.
2. Pilih **watsonx.ai** lalu kaitkan dengan project.

![Associate Service](https://github.com/user-attachments/assets/3e22c81c-288c-445c-a5c8-6cffb5976012)

---

### Step 3 — Menambahkan *Asset* Baru
1. Masuk ke tab **Assets** dan klik **New Asset**.

![New Asset](https://github.com/user-attachments/assets/dda99a0c-7240-40e7-a747-428d6bc2d06b)

---

### Step 4 — Membuat Notebook
1. Pilih **Work with data and models in Python or R notebooks**.
2. Tekan **Create a notebook**.

![Create Notebook](https://github.com/user-attachments/assets/a921bad3-bfa5-4f4a-8b92-785f1a1c859a)

---

### Step 5 — Meng‑*upload* Notebook
1. Klik **Local File**.
2. Unggah file:  
   • `SalesAnalysis.ipynb`  
   • `SalesAnalysis_query.ipynb`
3. Klik **Create** untuk menyelesaikan.

![Upload Notebook](https://github.com/user-attachments/assets/99702f15-60bb-451e-9553-02ce43629a34)

![Notebook List](https://github.com/user-attachments/assets/1fd1dd77-c63d-4e54-9199-f60c115f8ef7)

---

### Step 6 — Mengonfigurasi API Key
1. Masukkan kunci yang diperlukan di sel konfigurasi.
2. Buat **IBM Cloud API Key** baru *atau* gunakan milik tim, lalu isi parameter `api_key`.
3. Pastikan `api_base` sesuai dengan instans watsonx Anda.
4. `DB_Password` tersedia di *DB Connection Details.boxnote*.

![API Key](https://github.com/user-attachments/assets/bc611d4d-18ea-4d1f-bf0b-5997581d987e)

> Anda juga dapat membuat API key melalui beranda IBM Cloud dan menyimpannya di mesin lokal.

![Create Key](https://github.com/user-attachments/assets/9d1f90ef-4da0-493b-bcca-07887e609c56)

---

### Step 7 — Menjalankan Notebook
1. Eksekusi sel‐sel notebook secara berurutan.
2. Beberapa kueri uji sudah disediakan sebagai komentar—hapus `#` dan jalankan untuk menguji hasil.

![Run Notebook](https://github.com/user-attachments/assets/7a5fedd0-7f73-40db-a5eb-4cfdcb92bdce)

---

## 🎉 Selesai!
Selamat! Anda telah berhasil membuat **Sales Analyzer Agent** berbasis **watsonx.ai** dan **Crew AI**.  
Happy Coding! 🚀🎯
