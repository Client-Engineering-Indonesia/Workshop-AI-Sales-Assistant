# AI Agent Labs with **watsonx.ai**

Dokumen ini mencakup **dua** lab terpisah:

1. **Lab 1 — Membangun *Sales Analyzer Agent* dengan watsonx.ai & Crew AI**  
2. **Lab 2 — Menghubungkan AI Agent ke watsonx Orchestrate**

---

## Lab 1 — Membangun *Sales Analyzer Agent* dengan watsonx.ai & Crew AI

Pada lab ini, kita akan membuat **Sales Analyzer Agent** dengan memanfaatkan *watsonx.AI Agent Lab* dan framework **Crew AI**. Agent ini akan menganalisis data penjualan sebuah produk untuk membantu proses procurement.

> **Catatan** File‐file yang diperlukan dapat diunduh dari folder “📂 *to‑be‑provided*”.

### Tahapan Pembuatan Agent

#### Step 1 — Membuat *Project*
1. Jika ini pertama kali Anda menggunakan akun ini, buatlah **Project** baru sebelum membuka Agent Lab. 
2. Jika sudah punya, Anda boleh memakai project yang ada.

![Project](https://github.com/user-attachments/assets/1282049d-f55e-47f6-9ff9-e176dd3e4af8)

#### Step 2 — Mengasosiasikan watsonx.ai Runtime
1. Buka **Manage → Services & Integrations → Associate Service**.
2. Pilih **watsonx.ai** lalu kaitkan dengan project.

![Associate Service](https://github.com/user-attachments/assets/3e22c81c-288c-445c-a5c8-6cffb5976012)

#### Step 3 — Menambahkan *Asset* Baru
1. Masuk ke tab **Assets** dan klik **New Asset**.

![New Asset](https://github.com/user-attachments/assets/dda99a0c-7240-40e7-a747-428d6bc2d06b)

#### Step 4 — Membuat Notebook
1. Pilih **Work with data and models in Python or R notebooks**.
2. Tekan **Create a notebook**.

![Create Notebook](https://github.com/user-attachments/assets/a921bad3-bfa5-4f4a-8b92-785f1a1c859a)

#### Step 5 — Meng‑*upload* Notebook
1. Klik **Local File**.
2. Unggah file:
   * `SalesAnalysis.ipynb`
   * `SalesAnalysis_query.ipynb`
3. Klik **Create** untuk menyelesaikan.

![Upload Notebook](https://github.com/user-attachments/assets/99702f15-60bb-451e-9553-02ce43629a34)

![Notebook List](https://github.com/user-attachments/assets/1fd1dd77-c63d-4e54-9199-f60c115f8ef7)

#### Step 6 — Mengonfigurasi API Key
1. Masukkan kunci yang diperlukan di sel konfigurasi.
2. Buat **IBM Cloud API Key** baru *atau* gunakan milik tim, lalu isi parameter `api_key`.
3. Pastikan `api_base` sesuai dengan instans watsonx Anda.
4. `DB_Password` tersedia di *DB Connection Details.boxnote*.

![API Key](https://github.com/user-attachments/assets/bc611d4d-18ea-4d1f-bf0b-5997581d987e)

> Anda juga dapat membuat API key melalui beranda IBM Cloud dan menyimpannya di mesin lokal.

![Create Key](https://github.com/user-attachments/assets/9d1f90ef-4da0-493b-bcca-07887e609c56)

#### Step 7 — Menjalankan Notebook
1. Eksekusi sel‐sel notebook secara berurutan.
2. Beberapa kueri uji sudah disediakan sebagai komentar—hapus `#` dan jalankan untuk menguji hasil.

![Run Notebook](https://github.com/user-attachments/assets/7a5fedd0-7f73-40db-a5eb-4cfdcb92bdce)

#### 🎉 Selesai!
Selamat! Anda telah berhasil membuat **Sales Analyzer Agent** berbasis **watsonx.ai** dan **Crew AI**.  
Happy Coding! 🚀🎯

---

## Lab 2 — Menghubungkan AI Agent ke watsonx Orchestrate

### Tujuan
Solusi rule‑based atau AI generatif saja sering tidak cukup untuk menangani alur kerja kompleks yang melibatkan banyak langkah. Dengan **watsonx Orchestrate**, kita dapat menggabungkan beberapa AI agent—masing‑masing dirancang untuk tugas spesifik—ke dalam satu orkestrator yang mengotomatisasi proses end‑to‑end.

Pada lab ini Anda akan menghubungkan AI agent (yang berjalan di **Code Engine**, mirip konsep AWS Lambda) ke watsonx Orchestrate. Syaratnya: agent harus menyediakan endpoint **`POST /chat/completions`** sesuai spesifikasi Orchestrate.

> **Arsitektur singkat**: Backend Python FastAPI di Code Engine memanggil endpoint `ai_service` & `ai_service_stream` dari AI agent. Diagram alur:
>
> ![Diagram](https://github.com/user-attachments/assets/2104bca3-01c9-4680-9958-264db0c306a8)

---

### Step 0 — Menyiapkan Aplikasi AI di watsonx.ai
Agar fokus pada integrasi, sebuah AI agent lengkap (dengan Google Search & Document Search) sudah disediakan. Lihat dokumentasi repositori untuk detail implementasi.

### Step 1 — Membuat Code Engine Project
Kami juga sudah menyiapkan *wrapper* aplikasi dan menerapkannya di IBM Code Engine. Jika ingin mempelajari proses build & deploy, cek dokumentasi terkait.

### Step 2 — Mendaftarkan Endpoint sebagai **External Agent** di Orchestrate
1. Buka **AI agent configuration** dari hamburger menu kiri‑atas.
   ![Hamburger](https://github.com/user-attachments/assets/7bf1bea5-89c1-4c43-94ce-01685da513d6)
2. Pilih **Agents** → klik **Add agent**.
3. Isi form:
   * **Display Name**: `[Inisial Nama] Supplier Research`
   * **Description**: AI agent yang menggunakan Google Search & dokumen supplier untuk menjawab pertanyaan procurement.
   * **API Key**: bebas (string apa saja)
   * **Service Instance URL**:  
     `https://bahasa-agent-supplier-research.1tzeky9wts20.us-south.codeengine.appdomain.cloud/chat/completions`
   
   ![URL](https://github.com/user-attachments/assets/6a853ea9-26a6-49f3-8e8b-303292c11060)
4. **Menampilkan chain‑of‑thought** *(optional)*: setelah agent dibuat, klik namanya → aktifkan *Show thinking in chat*.
   ![CoT](https://github.com/user-attachments/assets/bf9bb2a2-1f43-4e93-b0ae-72ae728c2d00)

### Step 3 — Menguji Agent di **AI Chat**
1. Pilih **Chat** di sidebar watsonx Orchestrate.
2. Ketik pertanyaan dengan *mention* agent, misalnya:
   ```text
   @RA-supplier-research Pemasok mana yang lebih layak untuk membeli produk Xtralife antara Excelentia Supplies dan Global Office Supplies? Berikan daftar kelebihan dan kekurangan.
   ```
   ![Chat 1](https://github.com/user-attachments/assets/852619b9-af4b-4703-b62c-1ea7337516a8)
3. Contoh lain:
   ```text
   @Supplier Research Supplier mana yang harus saya pilih? Saya butuh cepat dan urgent.
   ```
   ![Chat 2](https://github.com/user-attachments/assets/06487675-d08c-4b83-a836-c3b0719d1393)

---

### Referensi
* Lab & kode backend asli: <https://github.com/rc-ibm/watsonx-orchestrate-developer-toolkit/tree/main/external_agent>
* Artikel tentang agent di Orchestrate: <https://heidloff.net/article/watsonx-orchestrate-agent-agents/>

![Ref](https://github.com/user-attachments/assets/a2531607-735c-4ae3-994c-4799dec156c7)

---

## 🎯 Penutup
Dengan menyelesaikan **Lab 2** ini, Anda sekarang mampu:
1. Menyediakan AI agent sebagai layanan eksternal (endpoint `/chat/completions`).
2. Mendaftarkan & mengonfigurasi agent di watsonx Orchestrate.
3. Mendorong kolaborasi multi‑agent untuk alur kerja procurement yang kompleks.

Selamat bereksperimen! 🚀
